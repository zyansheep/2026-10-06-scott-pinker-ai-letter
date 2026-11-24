import json,re,sys,statistics as st
from html.parser import HTMLParser
h=json.load(open(sys.argv[1]))['parse']['text']
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tables=[];s.row=None;s.cell=None;s.t=None;s.skip=0
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag=='table': s.t=[]; s.tables.append(s.t)
        elif tag=='tr' and s.t is not None: s.row=[]; s.t.append(s.row)
        elif tag in('td','th') and s.row is not None: s.cell=[]; s.row.append(s.cell); s.sv=a.get('data-sort-value')
        elif tag=='sup' : s.skip+=1
        if tag in('td','th') and s.row is not None: s.cell.append(('SV',a.get('data-sort-value')))
    def handle_endtag(s,tag):
        if tag in('td','th'): s.cell=None
        elif tag=='sup': s.skip-=1
        elif tag=='table': s.t=None
    def handle_data(s,d):
        if s.cell is not None and not s.skip: s.cell.append(d)
p=P(); p.feed(h)
t=[t for t in p.tables if t and any('P(doom)' in ''.join(x for x in c if isinstance(x,str)) for c in t[0])][0]
rows=[]
for r in t[1:]:
    cells=[]; 
    for c in r:
        txt=''.join(x for x in c if isinstance(x,str)).strip(); sv=[x[1] for x in c if isinstance(x,tuple)][0]
        cells.append((re.sub(r'\s+',' ',txt),sv))
    rows.append(cells)
json.dump(rows,open('rows2.json','w'))
print(len(t[0]),[ ''.join(x for x in c if isinstance(x,str)) for c in t[0]])
for r in rows: print(r[0][0],'|',r[2][0],'|',r[2][1],'|',r[3][0] if len(r)>3 else '')
print(len(rows))
