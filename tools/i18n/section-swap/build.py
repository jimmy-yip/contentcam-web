# build.py <lang> : applies scratchpad/dg/<lang>.py dict T to <lang>/vs/dualgram/index.html
import os,re,sys,json,runpy,html
S=os.path.dirname(os.path.abspath(__file__)); os.chdir(os.path.expanduser('~/contentcam-web'))
l=sys.argv[1]; T=runpy.run_path(os.path.join(S,l+'.py'))['T']
p=f'{l}/vs/dualgram/index.html'; t=open(p,encoding='utf-8').read()
a0=t.index('<article'); head,body=t[:a0],t[a0:]
def rep_p_after(s,pos,new_inner):
    i=s.index('<p',pos); j=s.index('</p>',i)+4
    return s[:i]+new_inner+s[j:]
# 1 byline
i=body.index('<p class="byline">'); j=body.index('</p>',i)+4
body=body[:i]+f'<p class="byline">{T["byline"]}</p>'+body[j:]
# 2 disclosure (next <p>) -> disclosure + tested summary
k=body.index('<p>',j); e=body.index('</p>',k)+4
body=body[:k]+f'<p>{T["disc"]}</p>\n      <p><strong>{T["tested_label"]}</strong> {T["summary"]}</p>'+body[e:]
H=lambda b:[m.start() for m in re.finditer(r'<h2>',b)]
# 3 main differences list items 1,2,3
h=H(body); seg=body[h[0]:h[1]]
lis=list(re.finditer(r'<li>.*?</li>',seg,re.S)); assert len(lis)==5,len(lis)
for idx,key in [(3,'li_controls'),(2,'li_vertical'),(1,'li_android')]:
    m=lis[idx]; seg=seg[:m.start()]+f'<li>{T[key]}</li>'+seg[m.end():]
body=body[:h[0]]+seg+body[h[1]:]
# 4 section 2: 5th <p><strong>
h=H(body); seg=body[h[1]:h[2]]
ps=list(re.finditer(r'<p><strong>.*?</p>',seg,re.S)); assert len(ps)==5,len(ps)
m=ps[4]; seg=seg[:m.start()]+f'<p>{T["p_fullcam"]}</p>'+seg[m.end():]
body=body[:h[1]]+seg+body[h[2]:]
# 5 section 3 first p
h=H(body); seg=body[h[2]:h[3]]; m=re.search(r'<p>.*?</p>',seg,re.S)
seg=seg[:m.start()]+f'<p>{T["p_builtfor"]}</p>'+seg[m.end():]; body=body[:h[2]]+seg+body[h[3]:]
# 6 table body
i=body.index('<tbody>'); j=body.index('</tbody>')+8
rows='\n'.join(f'          <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in T['rows'])
body=body[:i]+'<tbody>\n'+rows+'\n        </tbody>'+body[j:]
# 7 insert test section before h2[4]
FIG=[('dualgram-4k-60fps-not-supported.webp',1000,889),('dualgram-device-overloaded-front-720.webp',1000,137),('dualgram-cinematic-preview-lag-4k30-warning.webp',1000,945),('dualgram-pro-features.webp',1000,676)]
figs=''.join(f'      <figure>\n        <img src="/assets/vs/dualgram/{f}" alt="{alt}" width="{w}" height="{hh}" loading="lazy" decoding="async">\n        <figcaption>{cap}</figcaption>\n      </figure>\n' for (f,w,hh),(alt,cap) in zip(FIG,T['figs']))
lis=''.join(f'        <li><strong>{a}</strong> {b}</li>\n' for a,b in T['test_lis'])
sec=f'<h2>{T["test_h2"]}</h2>\n      <p>{T["test_intro"]}</p>\n      <ul>\n{lis}      </ul>\n      <p>{T["reviews"]}</p>\n{figs}      <p>{T["suits"]}</p>\n\n      '
h=H(body); body=body[:h[4]]+sec+body[h[4]:]
# 8 4K section prefix
h=H(body); i=body.index('<p>',h[5])+3; body=body[:i]+T['fourk_prefix']+' '+body[i:]
# 9 FAQ answers (h3 index 1 android, 3 separate, 4 vertical)
h3=[m.start() for m in re.finditer(r'<h3>',body)]; assert len(h3)==5
for idx,key in [(4,'faq_vertical'),(3,'faq_separate'),(1,'faq_android')]:
    i=body.index('<p>',h3[idx]); j=body.index('</p>',i)+4; body=body[:i]+f'<p>{T[key]}</p>'+body[j:]
# 10 sources prefix: last byline p
i=body.rindex('<p class="byline">'); c=min([x for x in (body.find(':',i),body.find('：',i)) if x>0])+1
body=body[:c]+' '+T['sources_prefix']+body[c:]
t=head+body
# 11 JSON-LD FAQ
def plain(s): return html.unescape(re.sub(r'<[^>]+>','',s))
def fix(o):
    if isinstance(o,dict):
        if o.get('@type')=='FAQPage':
            me=o['mainEntity']; assert len(me)==5
            me[1]['acceptedAnswer']['text']=plain(T['faq_android']); me[3]['acceptedAnswer']['text']=plain(T['faq_separate']); me[4]['acceptedAnswer']['text']=plain(T['faq_vertical'])
            me.insert(1,{"@type":"Question","name":T['fourk_q'],"acceptedAnswer":{"@type":"Answer","text":T['fourk_a']}}); return True
        return any(fix(v) for v in o.values())
    if isinstance(o,list): return any(fix(v) for v in o)
    return False
done=False
for m in list(re.finditer(r'(<script type="application/ld\+json">)(.*?)(</script>)',t,re.S)):
    o=json.loads(m.group(2))
    if fix(o):
        new=m.group(1)+'\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n  '+m.group(3)
        t=t[:m.start()]+new+t[m.end():]; done=True; break
assert done
t=re.sub(r'"dateModified": "2026-\d\d-\d\d"','"dateModified": "2026-11-12"',t)
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',t,re.S): json.loads(m.group(1))
open(p,'w',encoding='utf-8').write(t); print(l,'ok')
