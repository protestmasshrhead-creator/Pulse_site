import json,os,re,sys,hashlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from extract import run

SP=os.environ['SP']; SRC=SP+'/src'
LANGS=[('ru','Русский','RU'),('en','English','EN'),('de','Deutsch','DE'),
       ('es','Español','ES'),('cs','Čeština','CS'),('sk','Slovenčina','SK'),
       ('ro','Română','RO'),('hu','Magyar','HU')]
SEL={'ru':'Выбрать язык','en':'Select language','de':'Sprache wählen',
     'es':'Elegir idioma','cs':'Vybrat jazyk','sk':'Vybrať jazyk',
     'ro':'Alegeți limba','hu':'Nyelv választása'}
SITE='https://pulse-call.com'

LANGCSS = """
.lang-sw{position:relative;flex:none;margin-left:auto}
.lang-btn{display:inline-flex;align-items:center;gap:8px;cursor:pointer;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.22);color:#EAF1FB;
  font:inherit;font-size:14px;font-weight:600;padding:8px 12px;border-radius:999px;transition:.16s;line-height:1}
.lang-btn:hover{border-color:rgba(255,122,26,.7)}
.lang-btn svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2}
.lang-btn .car{width:10px;height:10px;opacity:.75;transition:transform .18s}
.lang-sw.open .lang-btn .car{transform:rotate(180deg)}
.lang-menu{position:absolute;top:calc(100% + 8px);right:0;min-width:200px;z-index:80;
  background:#0E1E3C;border:1px solid rgba(255,255,255,.2);border-radius:14px;padding:6px;
  box-shadow:0 18px 44px rgba(0,0,0,.45)}
.lang-menu[hidden]{display:none}
.lang-menu a{display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding:10px 12px;border-radius:10px;text-decoration:none;color:#DCE7F6;font-size:14px;transition:.14s}
.lang-menu a:hover{background:rgba(76,141,246,.18);color:#fff}
.lang-menu a[aria-current="true"]{background:rgba(255,122,26,.16);color:#fff}
.lang-menu b.code{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.1em;font-weight:700}
@media(max-width:600px){.lang-btn span.lbl{display:none}}
"""

LANGJS = """
<script>
(function(){
  var sw=document.querySelector('.lang-sw'); if(!sw) return;
  var btn=sw.querySelector('.lang-btn'), menu=sw.querySelector('.lang-menu');
  function close(){menu.hidden=true;sw.classList.remove('open');btn.setAttribute('aria-expanded','false');}
  btn.addEventListener('click',function(e){e.stopPropagation();
    if(menu.hidden){menu.hidden=false;sw.classList.add('open');btn.setAttribute('aria-expanded','true');}else close();});
  document.addEventListener('click',function(e){if(!sw.contains(e.target))close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  menu.addEventListener('click',function(e){var a=e.target.closest('a[data-lang]');if(a){close();}});
})();
</script>
"""


def url_for(page,lang):
    d=os.path.dirname(page)
    p='/' if d=='' else '/'+d+'/'
    return p if lang=='ru' else '/'+lang+p

def find_block(src, start_pat):
    """находит <div ...> ... </div> с балансировкой вложенных div"""
    m=re.search(start_pat, src)
    if not m: return None
    i=m.end(); depth=1
    tag=re.compile(r'<(/?)div\b', re.I)
    while depth>0:
        t=tag.search(src, i)
        if not t: return None
        depth += -1 if t.group(1) else 1
        i=t.end()
    end=src.index('>', i-1)+1
    return m.start(), end

def lang_block(page, cur, indent):
    name=[n for c,n,_ in LANGS if c==cur][0]
    items=[]
    for c,n,code in LANGS:
        href=url_for(page,c)
        attr=' aria-current="true"' if c==cur else f' hreflang="{c}"'
        items.append(f'{indent}    <a href="{href}" data-lang="{c}"{attr}>{n}<b class="code">{code}</b></a>')
    return (f'{indent}<div class="lang-sw" data-lang="{cur}">\n'
      f'{indent}  <button type="button" class="lang-btn" aria-haspopup="true" aria-expanded="false" aria-label="{SEL[cur]}">\n'
      f'{indent}    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18 15 15 0 0 1 0-18z"/></svg>\n'
      f'{indent}    <span class="lbl">{name}</span>\n'
      f'{indent}    <svg class="car" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>\n'
      f'{indent}  </button>\n'
      f'{indent}  <div class="lang-menu" role="menu" hidden>\n'
      + '\n'.join(items) + '\n'
      f'{indent}  </div>\n'
      f'{indent}</div>')

def head_links(page, cur):
    out=[f'<link rel="canonical" href="{SITE}{url_for(page,cur)}">']
    for c,_,_ in LANGS:
        out.append(f'<link rel="alternate" hreflang="{c}" href="{SITE}{url_for(page,c)}">')
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}{url_for(page,"ru")}">')
    return '\n'.join(out)+'\n'

def translate(src, segs, attrs, tr):
    for s in sorted(segs, key=lambda x:-x['start']):
        raw=s['text']; key=raw.strip()
        if key in tr:
            lead=raw[:len(raw)-len(raw.lstrip())]; tail=raw[len(raw.rstrip()):]
            val=tr[key]
            if s.get('js'):                      # экранируем кавычку-обрамитель
                val=val.replace(s['quote'], '\\'+s['quote'])
            src=src[:s['start']]+lead+val+tail+src[s['end']:]
    for a in attrs:
        k=a['text'].strip()
        if k in tr: src=src.replace(f'{a["attr"]}="{a["text"]}"', f'{a["attr"]}="{tr[k]}"')
    return src


def externalise(src, page):
    """выносит <style> и скрипт переключателя в общие файлы /assets/"""
    depth='../'*len(os.path.dirname(page).split('/')) if os.path.dirname(page) else ''
    m=re.search(r'<style>(.*?)</style>', src, re.S)
    if m:
        css=m.group(1)
        h=hashlib.md5(css.encode()).hexdigest()[:10]
        os.makedirs('assets/css', exist_ok=True)
        path=f'assets/css/{h}.css'
        if not os.path.exists(path): open(path,'w',encoding='utf-8').write(css.strip()+'\n')
        src=src[:m.start()]+f'<link rel="stylesheet" href="/{path}">'+src[m.end():]
    # скрипт переключателя языков одинаков во всех языках и на всех страницах
    for mm in list(re.finditer(r'<script>(.*?)</script>', src, re.S))[::-1]:
        js=mm.group(1)
        if '.lang-sw' not in js: continue
        os.makedirs('assets/js', exist_ok=True)
        if not os.path.exists('assets/js/lang.js'):
            open('assets/js/lang.js','w',encoding='utf-8').write(js.strip()+'\n')
        src=src[:mm.start()]+'<script src="/assets/js/lang.js" defer></script>'+src[mm.end():]
    return src

def build(lang):
    tr={} if lang=='ru' else json.load(open(f'{SP}/dict/{lang}.json', encoding='utf-8'))
    pages=[]
    for root,dirs,files in os.walk(SRC):
        rel=os.path.relpath(root,SRC)
        if rel.startswith('legal'): continue
        for f in files:
            if f.endswith('.html'):
                pages.append((os.path.join(rel,f) if rel!='.' else f).replace(os.sep,'/'))
    n=0
    for page in sorted(pages):
        srcpath=os.path.join(SRC,page)
        src,segs,attrs=run(srcpath)
        if lang!='ru': src=translate(src,segs,attrs,tr)
        src=re.sub(r'<html lang="ru"', f'<html lang="{lang}"', src, count=1)
        if lang!='ru':
            # юридические документы существуют только на английском в корне —
            # языковой префикс к ним не добавляем
            src=re.sub(r'href="/(?!/|legal/|assets/)', f'href="/{lang}/', src)
        # переключатель языков
        b=find_block(src, r'[ \t]*<div class="lang-sw"[^>]*>')
        if b:
            s0,e0=b
            indent=re.match(r'[ \t]*', src[s0:]).group(0)
            src=src[:s0]+lang_block(page,lang,indent)+src[e0:]
        else:
            # у страниц тестов упрощённая шапка без переключателя — добавляем его
            src=src.replace('</style>', LANGCSS+'</style>', 1)
            src=re.sub(r'(\n</div></header>)',
                       '\n'+lang_block(page,lang,'  ')+r'\1', src, count=1)
            src=src.replace('</body>', LANGJS+'</body>', 1)
        # ссылки в head
        src=re.sub(r'(<link rel="preconnect")', head_links(page,lang)+r'\1', src, count=1)
        # рабочие ссылки в меню языков
        src=src.replace("var a=e.target.closest('a[data-lang]');if(a){e.preventDefault();close();}",
                        "var a=e.target.closest('a[data-lang]');if(a){close();}")
        src=src.replace("    var a=e.target.closest('a[data-lang]'); if(!a) return;\n    e.preventDefault();\n",
                        "    var a=e.target.closest('a[data-lang]'); if(!a) return;\n")
        src=src.replace("curLang()==='en'", "false")
        src=externalise(src, page)
        out = page if lang=='ru' else os.path.join(lang,page)
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        open(out,'w',encoding='utf-8').write(src); n+=1
    print(f"{lang}: собрано {n} страниц")

if __name__=='__main__': build(sys.argv[1])
