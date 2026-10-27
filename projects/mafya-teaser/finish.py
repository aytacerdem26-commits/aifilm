#!/usr/bin/env python3
"""HESAP teaser son adımı: diyalog altyazıları (ölçülen konuşma zamanlarıyla) + 2 sn "HESAP / Yakında" kartı.

Girdi: final/mafya-teaser.mp4 (assemble.py --no-music çıktısı, 30 sn, 1080x1920)
Çıktı: final/hesap-teaser.mp4 (altyazılı), final/hesap-teaser_nosubs.mp4
"""
import subprocess
from pathlib import Path

PROJ = Path(__file__).resolve().parent
FINAL = PROJ / "final"
SRC = FINAL / "mafya-teaser.mp4"
FONT_BOLD = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FONT_LIGHT = "/usr/share/fonts/opentype/inter/Inter-Light.otf"
TAIL = 2.0

# (başlangıç, bitiş, metin) — film zaman çizelgesinde; klip başı + ölçülen konuşma aralığı
SUBS = [
    (1.5, 3.6, "Bu gece biri beni sattı, Kenan."),   # S01 0–5 sn, konuşma 1.5–3.3
    (9.3, 11.0, "Yere yat!"),                         # S03 9–14 sn
    (27.8, 29.6, "Hesap kapandı, Reis."),             # S06 24–30 sn, konuşma 3.8–4.9
]


def ts(s):
    ms = round(s * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{sec:02},{ms:03}"


def main():
    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(SRC)]).decode())
    total = dur + TAIL
    srt = FINAL / "hesap-teaser.srt"
    srt.write_text("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(SUBS, 1)),
                   encoding="utf-8")

    t0 = dur + 0.15
    fade = f"alpha='if(lt(t,{t0 + 0.4:.2f}),(t-{t0:.2f})/0.4,1)'"
    card = (f",drawtext=fontfile={FONT_BOLD}:text='HESAP':fontcolor=white:fontsize=170:"
            f"x=(w-text_w)/2:y=(h-text_h)/2-60:enable='gte(t,{t0:.2f})':{fade}"
            f",drawtext=fontfile={FONT_LIGHT}:text='Yakında':fontcolor=0xD7263D:fontsize=64:"
            f"x=(w-text_w)/2:y=(h/2)+90:enable='gte(t,{t0 + 0.3:.2f})':{fade}")
    base_v = (f"tpad=stop_duration={TAIL}:stop_mode=add:color=black,"
              f"fade=t=out:st={dur - 0.4:.3f}:d=0.4")
    af = f"apad=whole_dur={total:.3f},afade=t=out:st={dur - 0.3:.3f}:d={TAIL}"
    for name, subs in (("hesap-teaser_nosubs.mp4", False), ("hesap-teaser.mp4", True)):
        vf = base_v + card
        if subs:
            vf = (base_v + f",subtitles={srt.as_posix()}:force_style='FontName=Inter,FontSize=13,Bold=1,"
                  "Outline=1.5,Shadow=0,MarginV=70,Alignment=2'" + card)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(SRC), "-vf", vf, "-af", af,
                        "-t", f"{total:.3f}", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
                        "-r", "24", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
                        str(FINAL / name)], check=True)
    print(f"total {total:.2f} s")


if __name__ == "__main__":
    main()
