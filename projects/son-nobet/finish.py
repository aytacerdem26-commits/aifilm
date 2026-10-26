#!/usr/bin/env python3
"""Kurgu son adımı: baş 1 sn siyah + fade-in, son 2 sn siyah + başlık, düzeltilmiş altyazı."""
import subprocess, sys
from pathlib import Path
final = Path("/home/user/aifilm/projects/son-nobet/final")
src = final / "the-last-watch_nosubs_raw.mp4"
HEAD, TAIL = 1.0, 2.0
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",str(src)]).decode())
total = HEAD + dur + TAIL
# (shot start in script timeline, speech end in V.O. file, text, next shot start)
rows = [
 (0.0, 6.71, "Forty-one years. The same light. The same sea.", 7.5),
 (7.5, 3.36, "Tomorrow, a machine keeps the watch.", 14.5),
 (14.5, 3.34, "The light can turn itself now, they said.", 21.5),
 (21.5, 2.89, "I never knew who my light reached.", 28.5),
 (35.5, 4.70, "No ship ever sailed out there. Nothing ever did.", 41.5),
 (41.5, 5.05, "That was my signal. Two short... one long.", 49.5),
 (56.5, 6.78, "Forty-one years looking down. Tonight, I go down.", 64.5),
 (79.5, 4.80, "All the light I ever gave away... came back.", 86.5),
 (94.0, 1.22, "To take me home.", 99.5),
 (107.5, 3.28, "Let the sea keep its own light now.", 115.5),
]
def ts(s):
    ms=round(s*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); se,ms=divmod(ms,1000)
    return f"{h:02}:{m:02}:{se:02},{ms:03}"
out=[]
for i,(st,se,txt,nxt) in enumerate(rows,1):
    a=st+0.2; b=min(a+max(se+0.8,2.0), nxt-0.05)
    out += [str(i), f"{ts(a+HEAD)} --> {ts(b+HEAD)}", txt, ""]
srt = final/"the-last-watch.srt"
srt.write_text("\n".join(out), encoding="utf-8")

font = "/usr/share/fonts/opentype/inter/Inter-ExtraLight.otf"
pic_end = HEAD + dur
t0, t1 = pic_end + 0.2, total
title = (f",drawtext=fontfile={font}:text='THE LAST WATCH':fontcolor=white:fontsize=72:"
         f"x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t,{t0:.2f},{t1:.2f})':"
         f"alpha='if(lt(t,{t0+0.5:.2f}),(t-{t0:.2f})/0.5,if(gt(t,{t1-0.5:.2f}),({t1:.2f}-t)/0.5,1))'") if Path(font).exists() else ""
base_v = (f"tpad=start_duration={HEAD}:start_mode=add:color=black:stop_duration={TAIL}:stop_mode=add:color=black,"
          f"fade=t=in:st={HEAD}:d=1.5,fade=t=out:st={pic_end-1.0:.3f}:d=1.0")
af = (f"adelay={int(HEAD*1000)}:all=1,apad=whole_dur={total:.3f},afade=t=in:st={HEAD}:d=1.0,"
      f"afade=t=out:st={pic_end:.3f}:d={TAIL}")
for name, subs in (("the-last-watch_nosubs.mp4", False), ("the-last-watch.mp4", True)):
    vf = base_v + (f",subtitles={srt.as_posix()}:force_style='FontName=Inter,FontSize=15,Outline=1,Shadow=0,MarginV=22'" if subs else "") + title
    cmd = ["ffmpeg","-v","error","-y","-i",str(src),"-vf",vf,"-af",af,"-t",f"{total:.3f}",
           "-c:v","libx264","-crf","18","-preset","medium","-pix_fmt","yuv420p","-r","24",
           "-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",str(final/name)]
    print("$"," ".join(cmd)); subprocess.run(cmd, check=True)
print("total", total)
