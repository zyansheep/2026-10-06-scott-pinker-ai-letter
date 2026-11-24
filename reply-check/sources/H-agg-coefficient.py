import csv,collections,re,sys
rows=list(csv.DictReader(open('/tmp/rc-H/cg.csv',encoding='utf-8')))
def amt(s):
    s=re.sub(r'[^\d.]','',s or ''); return float(s) if s else 0.0
def yr(d):
    m=re.search(r'(\d{4})',d or ''); return int(m.group(1)) if m else None
GH={'GiveWell-Recommended Charities','Human Health and Wellbeing','Global Health & Development','Global Health & Wellbeing','Global Health R&D','Global Aid Policy','South Asian Air Quality','Global Public Health Policy','Science for Global Health','Economic Growth in LMICs','Global Health & Wellbeing Opportunities'}
AI={'Navigating Transformative AI'}
GCR={'Global Catastrophic Risks','Global Catastrophic Risks Capacity Building','Biosecurity & Pandemic Preparedness','Science Supporting Biosecurity and Pandemic Preparedness'}
tab=collections.defaultdict(lambda: collections.defaultdict(float)); cnt=collections.defaultdict(int)
tot=collections.defaultdict(float); fa_year=collections.defaultdict(lambda: collections.defaultdict(float))
for r in rows:
    y=yr(r['Date']); a=amt(r['Amount']); f=r['Focus Area']
    if y is None: continue
    tot[y]+=a; fa_year[f][y]+=a
    g='GH' if f in GH else 'AI' if f in AI else 'GCR_other' if f in GCR else 'other'
    tab[y][g]+=a
    if f=='GiveWell-Recommended Charities': tab[y]['GW']+=a
print('year total GH(incl GW) GW AI GCR_other | GH% AI% | GH_exGW')
for y in sorted(tab):
    t=tot[y]; d=tab[y]
    print(y, f"{t/1e6:8.1f} GH {d['GH']/1e6:7.1f} GW {d['GW']/1e6:6.1f} AI {d['AI']/1e6:7.1f} GCRo {d['GCR_other']/1e6:7.1f} | GH {100*d['GH']/t if t else 0:4.1f}% AI {100*d['AI']/t if t else 0:4.1f}% AI+GCR {100*(d['AI']+d['GCR_other'])/t if t else 0:4.1f}%")
print()
for f in ['Navigating Transformative AI','Global Catastrophic Risks','Global Catastrophic Risks Capacity Building','GiveWell-Recommended Charities']:
    print(f,{y:round(v/1e6,1) for y,v in sorted(fa_year[f].items())})
