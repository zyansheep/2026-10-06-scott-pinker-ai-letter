import json,re,sys,statistics as st,urllib.request,subprocess
from html.parser import HTMLParser
def get(rid):
    u=f'https://en.wikipedia.org/w/api.php?action=parse&oldid={rid}&prop=text&format=json&formatversion=2'
    r=urllib.request.Request(u,headers={'User-Agent':'rc-fact-check/1.0 (research)'})
    return json.load(urllib.request.urlopen(r))['parse']['text']
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tables=[];s.row=None;s.cell=None;s.t=None;s.skip=0
    def handle_starttag(s,tag,a):
        if tag=='table': s.t=[]; s.tables.append(s.t)
        elif tag=='tr' and s.t is not None: s.row=[]; s.t.append(s.row)
        elif tag in('td','th') and s.row is not None: s.cell=[]; s.row.append(s.cell)
        elif tag in('sup','style'): s.skip+=1
    def handle_endtag(s,tag):
        if tag in('td','th'): s.cell=None
        elif tag in('sup','style'): s.skip-=1
        elif tag=='table': s.t=None
    def handle_data(s,d):
        if s.cell is not None and not s.skip: s.cell.append(d)
def run(rid):
    p=P(); p.feed(get(rid))
    t=[t for t in p.tables if t and any('P(doom)' in ''.join(c) for c in t[0])][0]
    vals=[]
    for r in t[1:]:
        txt=re.sub(r'\s+',' ',''.join(r[2])).strip().replace('–','-')
        txt=re.sub(r'\.mw-parser-output[^}]*}','',txt)
        txt=txt.replace('c. ','')
        core=txt.split('(')[0]
        n=[float(x) for x in re.findall(r'\d+(?:\.\d+)?',core)]
        if re.search(r'10-20% \(all',txt) or 'all-things' in txt: n=[10,20]
        if not n: print('??',txt); continue
        vals.append((min(n)+max(n))/2 if len(n)>1 else n[0])
    return len(vals),st.median(vals),sum(v>50 for v in vals),sum(v>=50 for v in vals)
for rid in sys.argv[1:]:
    print(rid,run(rid))
