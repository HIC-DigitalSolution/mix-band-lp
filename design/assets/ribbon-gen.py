# -*- coding: utf-8 -*-
import math
def bez(p,t):
    u=1-t;return (u**3*p[0][0]+3*u*u*t*p[1][0]+3*u*t*t*p[2][0]+t**3*p[3][0],
                  u**3*p[0][1]+3*u*u*t*p[1][1]+3*u*t*t*p[2][1]+t**3*p[3][1])
def dbez(p,t):
    u=1-t;return (3*u*u*(p[1][0]-p[0][0])+6*u*t*(p[2][0]-p[1][0])+3*t*t*(p[3][0]-p[2][0]),
                  3*u*u*(p[1][1]-p[0][1])+6*u*t*(p[2][1]-p[1][1])+3*t*t*(p[3][1]-p[2][1]))
def nz(s,i):
    x=math.sin((i+1)*12.9898+s*78.233)*43758.5453; return (x-math.floor(x)-0.5)*2

def strip(spine,w0,off0,off1,taper,endt,seed,barb=None,scallop=0.0):
    """off0→off1 でオフセットが変わる＝寄ったり開いたりする。endt で尖り切る位置を変える"""
    n=72;L=[];R=[]
    for i in range(n+1):
        t=i/n
        x,y=bez(spine,t);dx,dy=dbez(spine,t)
        m=math.hypot(dx,dy) or 1;nx,ny=-dy/m,dx/m
        tt=min(1.0,t/endt)
        w=w0*((1-tt)**taper)*(1+0.2*math.sin(math.pi*min(1,tt*1.6)))
        if w<0.25: w=0.25
        off=off0+(off1-off0)*(t**1.4)
        jl=nz(seed,i)*0.5;jr=nz(seed+9,i)*0.5
        if barb:
            bt,bw=barb; d=abs(t-bt)
            if d<0.045: jl-=bw*(1-d/0.045)
        if scallop: jr+=scallop*w0*0.07*math.sin(t*math.pi*5.0)
        cx,cy=x+nx*off,y+ny*off
        L.append((cx+nx*(w+jl),cy+ny*(w+jl)));R.append((cx-nx*(w+jr),cy-ny*(w+jr)))
    pts=L+R[::-1]
    return 'M%.1f,%.1f '%pts[0]+' '.join('L%.1f,%.1f'%p for p in pts[1:])+' Z'

def sym(sid,spine,strips,seed,back=None):
    parts=[]
    if back:
        w0,o0,o1=back
        parts.append('<path style="fill:var(--bc)" d="%s"/>'%strip(spine,w0,o0,o1,1.7,1.0,seed+41))
    for k,(w0,o0,o1,tp,et,cv,barb,sc) in enumerate(strips):
        parts.append('<path style="fill:var(--%s)" d="%s"/>'%(cv,strip(spine,w0,o0,o1,tp,et,seed+k*13,barb,sc)))
    return '<symbol id="rb-%s" viewBox="0 0 400 300">%s</symbol>'%(sid,''.join(parts))

# (w0, off開始, off終了, taper, 尖り切る位置, 色, 返し, 波打ち)
TRIO=(((-40,200),(60,152),(190,84),(430,40)),[
  (21,-30,-46,1.7,1.00,'c1',(0.10,8),0),
  (11, -6,-14,2.1,0.86,'c2',None,0),
  ( 7, 15, 30,2.4,0.70,'c3',None,0)])
QUAD=(((-30,26),(120,118),(200,222),(430,266)),[
  (13,-34,-52,1.9,0.92,'c1',None,0),
  (23, -8,-16,1.6,1.00,'c2',(0.12,9),0),
  ( 9, 16, 34,2.3,0.78,'c3',None,0),
  ( 6, 33, 56,2.6,0.62,'c4',None,0)])
CRES=(((-40,116),(110,198),(250,202),(430,114)),[
  (33,  0, -8,1.5,1.00,'c1',(0.14,10),1.0)])
NEEDLE=(((-40,240),(120,148),(250,92),(430,64)),[
  (12,  0,  6,2.2,0.95,'c1',(0.09,7),0)])
QUINT=(((-40,80),(110,182),(230,210),(430,168)),[
  (12,-46,-66,2.0,0.88,'c1',None,0),
  (22,-20,-30,1.6,1.00,'c2',(0.11,8),0),
  ( 9,  2,  8,2.3,0.80,'c3',None,0),
  ( 7, 20, 34,2.5,0.68,'c4',None,0),
  ( 5, 36, 60,2.8,0.56,'c5',None,0)])

SYMS=''.join([
 sym('trio',TRIO[0],TRIO[1],3,back=(9,-44,-62)),
 sym('quad',QUAD[0],QUAD[1],11),
 sym('crescent',CRES[0],CRES[1],17,back=(12,-26,-34)),
 sym('needle',NEEDLE[0],NEEDLE[1],23),
 sym('quint',QUINT[0],QUINT[1],29),
])
DEFS='''<pattern id="zb" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(64)">
  <rect width="14" height="14" fill="#f4e9eb"/>
  <path d="M0,0 C1.5,4 1,8 2,12 C2.5,13.5 2,14 2,14 L5,14 C4.5,10 5,6 4.2,3.5 C3.5,1.5 3.6,0 3.6,0 Z" fill="#2a1030"/>
  <path d="M8,1.5 C9.4,5 8.8,9 10,12.5 L11.4,12.5 C10.6,8.5 10.6,5 10,1.5 Z" fill="#2a1030"/></pattern>'''

P=[('trio','url(#zb)','#fff5f7','#d92785','','','#8e1a66','#2a1030'),
   ('quad','#fff5f7','url(#zb)','#ff8a1f','#d92785','','#5c154b','#2a1030'),
   ('quint','#fff5f7','url(#zb)','#ff8a1f','#e2c2c6','#d92785','#2a1030','#2a1030'),
   ('crescent','url(#zb)','','','','','#8e1a66','#2a1030'),
   ('needle','#ff8a1f','','','','','#2a1030','#2a1030'),
   ('trio','#2a1030','#8e1a66','url(#zb)','','','#d92785','#e2c2c6')]
cells=[]
for i,(sid,c1,c2,c3,c4,c5,bc,bg) in enumerate(P):
    cx=20+(i%2)*600; cy=34+(i//2)*310
    st=';'.join(['--c%d:%s'%(k+1,v) for k,v in enumerate([c1,c2,c3,c4,c5]) if v]+['--bc:%s'%bc])
    cells.append('<g transform="translate(%d,%d)"><text x="0" y="-8" font-family="sans-serif" font-size="12" fill="#6b5d61">%d %s</text>'
      '<clipPath id="k%d"><rect width="560" height="270"/></clipPath>'
      '<g clip-path="url(#k%d)"><rect width="560" height="270" fill="%s"/>'
      '<svg width="560" height="420" viewBox="0 0 400 300" style="overflow:visible"><use href="#rb-%s" style="%s"/></svg>'
      '</g></g>'%(cx,cy,i+1,sid,i,i,bg,sid,st))
sheet=('<svg xmlns="http://www.w3.org/2000/svg" width="1220" height="990" viewBox="0 0 1220 990">'
 '<defs>'+DEFS+SYMS+'</defs><rect width="1220" height="990" fill="#efe8e6"/>'+''.join(cells)+'</svg>')
B='/private/tmp/claude-501/-Users-rintaro-Job-LP-MIX-------LP/6d8f013f-9800-4ec9-b33a-59c225c855b0/scratchpad/'
open(B+'rb6.svg','w').write(sheet); open(B+'sprite5.svg','w').write('<defs>'+DEFS+SYMS+'</defs>')
print('ok')
