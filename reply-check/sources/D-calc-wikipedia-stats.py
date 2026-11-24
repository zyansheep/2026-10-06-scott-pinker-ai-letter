import json,re,statistics as st
rows=json.load(open('rows2.json'))
manual={ # displayed text cleaned by hand where parser garbled
 'Grady Booch':'0%','Lina Khan':'15%','Geoffrey Hinton':'10-20% (all-things-considered); >50% (independent impression)'}
data=[]
for r in rows:
    name=r[0][0]; disp=manual.get(name,r[2][0]); sv=r[2][1]
    disp=disp.replace('c. ','').replace('–','-')
    # ranges / numbers (take first 2 numbers before parenthetical)
    core=disp.split('(')[0]
    nums=[float(x) for x in re.findall(r'\d+(?:\.\d+)?',core.replace(',',''))]
    if name=='Geoffrey Hinton': nums=[10,20]  # all-things-considered
    lo=min(nums); hi=max(nums)
    mid=(lo+hi)/2
    if name=='Altman' or disp.startswith('>0'): mid=0.0  # ">0%" -> 0 floor (tiny)
    svn=float(sv.strip('%')) if sv else None
    data.append((name,disp,lo,hi,mid,svn))
for d in data: print(d)
def rep(lbl,vals):
    print(f'{lbl}: n={len(vals)} median={st.median(vals)} >50={sum(v>50 for v in vals)} >=50={sum(v>=50 for v in vals)}')
rep('A midpoint of range (Hinton ATC 10-20)',[d[4] for d in data])
rep('B Wikipedia sort values where present else midpoint',[d[5] if d[5] is not None else d[4] for d in data])
rep('C lower bound',[d[2] for d in data])
rep('D upper bound',[d[3] for d in data])
# Hinton independent >50 variant
v=[d[4] for d in data]; i=[d[0] for d in data].index('Geoffrey Hinton'); v2=v[:]; v2[i]=50; rep('E Hinton at 50 (indep.)',v2)
print('range top >50:',[ (d[0],d[1]) for d in data if d[3]>50])
print('mid >50:',[ (d[0],d[1],d[4]) for d in data if d[4]>50])
print('mid >=50:',[ (d[0],d[1],d[4]) for d in data if d[4]>=50 and not d[4]>50])
print(sorted(v))
