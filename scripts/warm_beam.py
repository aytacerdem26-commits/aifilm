# usage: warm_beam.py in.png out.png x y w h  -> beam/lamp pixels in box tinted to amber (#F2A541 family)
# usage: python3 -I qa/warm_beam.py <in.png> <out.png> x y w h  (1376x768 kare; kutudaki parlak huzme/lamba piksellerini aynı parlaklıkta amber tona çeker, kredisiz)
import sys,subprocess
src,dst=sys.argv[1],sys.argv[2]; x,y,w,h=map(int,sys.argv[3:7])
W,H=1376,768
raw=bytearray(subprocess.run(['ffmpeg','-loglevel','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout)
for j in range(y,y+h):
  for i in range(x,x+w):
    k=(j*W+i)*3; r,g,b=raw[k],raw[k+1],raw[k+2]
    L=0.299*r+0.587*g+0.114*b
    t=max(0.0,min(1.0,(L-55)/60.0))
    if t<=0: continue
    # target amber with same luminance
    tr,tg,tb=L*1.45,L*1.12,L*0.62
    raw[k]=min(255,int(r+(tr-r)*t)); raw[k+1]=min(255,int(g+(tg-g)*t)); raw[k+2]=max(0,int(b+(tb-b)*t))
subprocess.run(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-i','-',dst],input=bytes(raw))
