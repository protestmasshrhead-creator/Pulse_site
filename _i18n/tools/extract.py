import re, json, sys, os
from html.parser import HTMLParser

SKIP = {'script','style'}
ATTRS = ('placeholder','aria-label','alt','title','content','value')
CYR = re.compile(r'[а-яА-ЯёЁ]')

class Ex(HTMLParser):
    def __init__(s, src):
        super().__init__(convert_charrefs=False)
        s.src = src
        # offsets of each line start
        s.lines=[0]
        for m in re.finditer(r'\n', src): s.lines.append(m.end())
        s.depth=0; s.nodes=[]; s.attrs=[]
    def off(s):
        l,c = s.getpos(); return s.lines[l-1]+c
    def handle_starttag(s, tag, attrs):
        if tag in SKIP: s.depth+=1
        raw_start = s.off()
        raw_end = s.src.index('>', raw_start)+1
        raw = s.src[raw_start:raw_end]
        for k,v in attrs:
            if k in ATTRS and v and CYR.search(v):
                s.attrs.append({'tag':tag,'attr':k,'text':v})
    def handle_endtag(s, tag):
        if tag in SKIP and s.depth>0: s.depth-=1
    def handle_data(s, data):
        if s.depth>0: return
        if not data.strip(): return
        if not CYR.search(data): return
        start = s.off()
        # verify exact slice
        if s.src[start:start+len(data)] != data: return
        s.nodes.append({'start':start,'end':start+len(data),'text':data})

def js_strings(src):
    out=[]
    for m in re.finditer(r'<script[^>]*>(.*?)</script>', src, re.S):
        base=m.start(1); js=m.group(1)
        for sm in re.finditer(r'"((?:[^"\\\n]|\\.)*)"|\'((?:[^\'\\\n]|\\.)*)\'', js):
            val = sm.group(1) if sm.group(1) is not None else sm.group(2)
            if val and CYR.search(val):
                g = 1 if sm.group(1) is not None else 2
                out.append({'start':base+sm.start(g),'end':base+sm.end(g),'text':val,
                            'js':True,'quote':'"' if g==1 else "'"})
    return out

def run(path):
    src=open(path,encoding='utf-8').read()
    p=Ex(src); p.feed(src)
    segs = p.nodes + js_strings(src)
    segs.sort(key=lambda x:x['start'])
    # dedupe overlaps
    clean=[]; last=-1
    for s_ in segs:
        if s_['start']>=last: clean.append(s_); last=s_['end']
    return src, clean, p.attrs

if __name__=='__main__':
    src, segs, attrs = run(sys.argv[1])
    print(f"текстовых+JS сегментов: {len(segs)}, атрибутов: {len(attrs)}")
    for s_ in segs[:8]: print('  |', s_['text'].strip()[:80])
    for a in attrs[:5]: print('  @', a['attr'], '=', a['text'][:60])
