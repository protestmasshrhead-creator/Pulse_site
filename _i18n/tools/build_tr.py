import json,sys,os
sp=os.environ['SP']; lang=sys.argv[1]
idx=json.load(open(sp+'/index.json'))
out={}
for fn in sorted(os.listdir(sp+'/tr')):
    if not fn.startswith(lang+'.'): continue
    for line in open(sp+'/tr/'+fn,encoding='utf-8'):
        line=line.rstrip('\n')
        if not line.strip(): continue
        n,_,t=line.partition('\t')
        if n.strip().isdigit() and t: out[idx[n.strip()]]=t
json.dump(out, open(f'{sp}/{lang}.json','w'), ensure_ascii=False, indent=1)
missing=[k for k in idx if idx[k] not in out]
print(f"{lang}: переведено {len(out)}/{len(idx)}, не хватает {len(missing)}")
if missing: print("  первые пропуски:", sorted(int(m) for m in missing)[:15])
