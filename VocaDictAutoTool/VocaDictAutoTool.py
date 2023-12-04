import argparse
parser = argparse.ArgumentParser(
                    prog='VocaDictAutoTool',
                    description='Auto-splitting for some languages.')
parser.add_argument('vowel_l',help="Combinations of letters that represent vowel sounds, for example \"ang\" and \"a\" in pinyin Chinese. Separated by \",\".")
parser.add_argument('vowel_ph',help="All vowel phonemes, separated by \",\".")
parser.add_argument('uns_d',help="Unsplitted dictionary in format \"WORD\tphonemes separated by space\".")
parser.add_argument('nw_d',help="Output dictionary.")
parser.add_argument('-v',required=False,help="Verbose.",action="store_true")
args = parser.parse_args()
r=list("$&£¢€¥§∆√π✓™©^❤♫☎•°♨✈✣☏■☀➑✂☑✉☼☆✄✔✆—☁★♕")
vow=args.vowel_ph.split(',')
p=args.vowel_l.split(',')
vow.sort(key=len)
v=args.v
vow=vow[::-1]
def spl(a,ph,p,r,vow):
    phs=[]
    r2=[]
    p2=[]
    for i in range(len(ph)):
        phs.append(ph[i])	
        if ph[i] in vow:
            phs.append('-')
    for i in range(len(phs)-1,-1,-1):
        if phs[i]=='-':
            phs.pop(i)
            break
    phs=''.join(phs)	
    phs=phs.replace(' - ','-')
    while "  " in phs:
        phs=phs.replace("  "," ")
    phs=phs.replace("- ","-")
    phs = phs.replace(" -", "-")
    while "--" in a:
        a=a.replace("--","-")
    ta=phs.count('-')
    for i in range(len(p)):
        if len(p[i])>1:
            p2.append(r[i])
        else:
            p2.append(p[i])	
    for i in range (len(p2)):
        a=a.replace(p[i],p2[i])
    aa=''	
    for i in a:
        aa+=i
        if i in p2:
            if ta>0:
                aa+='-'
                ta-=1
    a=aa
    a=list(a)	
    a=''.join(a)		
    for i in range (len(p2)):
        a=a.replace(p2[i],p[i])
    return a,phs
f=open(args.uns_d,encoding="utf-8")
nf=open(args.nw_d, 'w',encoding="utf-8")
m=[]
err_l=open(
    'error.log','w',encoding="utf-8"
)
ers=[]
for k in f:
    if "," in k:
        k=k.split(",")
    else:
        k=k.split("	")
    w=k[0]
    a,phs=spl(w,k[-1],p,r,vow)
    if a.count('-')==phs.count('-'):
        m.append(f"{w},{a},{phs}")
        if v:
            print(f"{w},{a},{phs}")
    else:
        ers.append(f"ERROR: {a} and {phs.rstrip()} have different number of syllables. Try to process it manually.\n")
        if v:
            print(f"ERROR: {a} and {phs.rstrip()} have different number of syllables. Try to process it manually.\n")
f.close()
nf.write(",".join(vow)+'\n')
m=list(sorted(m))
for i in m:
    nf.write(i)
nf.close()
for i in ers:
    err_l.write(f'[{ers.index(i)+1}] {i}')
err_l.close()
print('Done!')