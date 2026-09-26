#!/usr/bin/env python3
"""Çekim listesindeki klipleri indirip ffmpeg ile final filme birleştirir.

Kullanım:
    python3 scripts/assemble.py projects/<slug> [--no-music] [--subs] [--vertical]

Beklenen yapı:
    projects/<slug>/03_cekim_listesi.json    (clip_file yerel yol, yoksa clip_url indirilir;
                                             clip_volume: klibin kendi sesi, 0 = sessiz)
    projects/<slug>/audio/vo_<SHOT_ID>.mp3   (opsiyonel, anlatıcı sesi)
    projects/<slug>/audio/music.mp3          (opsiyonel, müzik)
Çıktı:
    projects/<slug>/renders/  (indirilen ve normalize edilen klipler)
    projects/<slug>/final/<slug>.mp4 (+ .srt, _9x16.mp4)
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

RES = {
    "16:9": {"720p": (1280, 720), "1080p": (1920, 1080), "2160p": (3840, 2160)},
    "9:16": {"720p": (720, 1280), "1080p": (1080, 1920), "2160p": (2160, 3840)},
    "1:1": {"720p": (720, 720), "1080p": (1080, 1080), "2160p": (2160, 2160)},
}
XFADE_S = 0.5  # fade / dissolve geçiş süresi


def run(cmd):
    print("$", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True)


def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def has_audio(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=index", "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return bool(out)


def download(url, dest):
    if dest.exists():
        return
    print(f"indiriliyor: {url} -> {dest}")
    with urllib.request.urlopen(url) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def normalize(src, dst, dur, w, h, fps, volume=1.0):
    """Kırp, ölçekle/pad'le, fps'i eşitle, sessizse boş ses izi ekle."""
    vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
          f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={fps},format=yuv420p")
    cmd = ["ffmpeg", "-y", "-i", str(src)]
    if has_audio(src):
        amap = ["-map", "0:v:0", "-map", "0:a:0", "-af", f"volume={volume}"]
    else:
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        amap = ["-map", "0:v:0", "-map", "1:a:0"]
    cmd += amap + ["-t", f"{dur}", "-vf", vf, "-c:v", "libx264", "-preset", "medium",
                   "-crf", "18", "-c:a", "aac", "-ar", "48000", "-ac", "2", str(dst)]
    run(cmd)


def join_clips(clips, transitions, out, fps):
    """Klipleri geçişlerle birleştir; her çekimin film içindeki başlangıç zamanını döndür."""
    durs = [probe_duration(c) for c in clips]
    starts = [0.0]
    if len(clips) == 1:
        shutil.copy(clips[0], out)
        return starts, durs[0]

    inputs = []
    for c in clips:
        inputs += ["-i", str(c)]
    # Tüm girişleri aynı zaman tabanına getir (xfade/concat bunu şart koşar)
    fparts = [f"[{i}:v]setpts=PTS-STARTPTS,fps={fps},settb=1/{fps}[vi{i}];[{i}:a]asetpts=PTS-STARTPTS[ai{i}]"
              for i in range(len(clips))]
    vlast, alast, t = "vi0", "ai0", durs[0]
    for i in range(1, len(clips)):
        tr = transitions[i]
        if tr in ("fade", "dissolve"):
            kind = "fade" if tr == "dissolve" else "fadeblack"
            off = t - XFADE_S
            fparts.append(f"[{vlast}][vi{i}]xfade=transition={kind}:duration={XFADE_S}:offset={off:.3f}[v{i}]")
            fparts.append(f"[{alast}][ai{i}]acrossfade=d={XFADE_S}[a{i}]")
            starts.append(off)
            t = off + durs[i]
        else:  # cut
            fparts.append(f"[{vlast}][{alast}][vi{i}][ai{i}]concat=n=2:v=1:a=1[vc{i}][a{i}];[vc{i}]fps={fps},settb=1/{fps}[v{i}]")
            starts.append(t)
            t += durs[i]
        vlast, alast = f"v{i}", f"a{i}"
    run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fparts),
         "-map", f"[{vlast}]", "-map", f"[{alast}]",
         "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", str(out)])
    return starts, t


def srt_time(s):
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{sec:02},{ms:03}"


def write_srt(shots, starts, path):
    lines, n = [], 1
    for shot, st in zip(shots, starts):
        text = shot.get("dialogue") or shot.get("voiceover")
        if not text:
            continue
        end = st + float(shot["duration_s"]) - 0.1
        lines += [str(n), f"{srt_time(st + 0.1)} --> {srt_time(end)}", str(text), ""]
        n += 1
    path.write_text("\n".join(lines), encoding="utf-8")
    return n > 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", type=Path)
    ap.add_argument("--no-music", action="store_true")
    ap.add_argument("--subs", action="store_true", help="altyazıyı videoya yak")
    ap.add_argument("--vertical", action="store_true", help="ayrıca 9:16 kopya üret")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"{tool} bulunamadı; önce ffmpeg kurun.")

    proj = args.project
    data = json.loads((proj / "03_cekim_listesi.json").read_text(encoding="utf-8"))
    slug = data.get("slug") or proj.name
    ar, res, fps = data.get("aspect_ratio", "16:9"), data.get("resolution", "1080p"), data.get("fps", 24)
    w, h = RES.get(ar, RES["16:9"]).get(res, RES["16:9"]["1080p"])

    shots = [s for s in data["shots"] if s.get("status") != "cut"]
    missing = [s["id"] for s in shots
               if not (s.get("clip_file") and (proj / s["clip_file"]).exists()) and not s.get("clip_url")]
    if missing:
        sys.exit(f"klibi olmayan çekimler: {', '.join(missing)}")

    renders, final, audio = proj / "renders", proj / "final", proj / "audio"
    renders.mkdir(exist_ok=True)
    final.mkdir(exist_ok=True)

    norm = []
    for s in shots:
        if s.get("clip_file") and (proj / s["clip_file"]).exists():
            raw = proj / s["clip_file"]
        else:
            # URL değişirse (yeniden üretim) yeni dosya indirilsin diye adına URL özeti eklenir
            tag = hashlib.sha1(s["clip_url"].encode()).hexdigest()[:8]
            raw = renders / f"{s['id']}_{tag}_raw.mp4"
            download(s["clip_url"], raw)
        out = renders / f"{s['id']}.mp4"
        normalize(raw, out, float(s["duration_s"]), w, h, fps, s.get("clip_volume", 1.0))
        norm.append(out)

    transitions = [s.get("transition_in", "cut") for s in shots]
    picture = renders / "_picture.mp4"
    starts, total = join_clips(norm, transitions, picture, fps)

    # Ses miksi: klip sesi + V.O. (çekim başlangıcına) + müzik (ducking ile)
    inputs, fparts, mix = ["-i", str(picture)], [], ["[0:a]"]
    idx = 1
    for s, st in zip(shots, starts):
        vo = audio / f"vo_{s['id']}.mp3"
        if vo.exists():
            inputs += ["-i", str(vo)]
            ms = int((st + 0.2) * 1000)
            fparts.append(f"[{idx}:a]adelay={ms}|{ms},volume=1.0[vo{idx}]")
            mix.append(f"[vo{idx}]")
            idx += 1
    music = audio / "music.mp3"
    if music.exists() and not args.no_music:
        inputs += ["-stream_loop", "-1", "-i", str(music)]
        fo = max(total - 2, 0)
        fparts.append(f"[{idx}:a]atrim=0:{total:.3f},volume=0.25,afade=t=in:d=1.5,"
                      f"afade=t=out:st={fo:.3f}:d=2[mus]")
        mix.append("[mus]")
    fparts.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0,alimiter=limit=0.95[aout]")

    srt = final / f"{slug}.srt"
    has_subs = write_srt(shots, starts, srt)
    vmap = "0:v"
    if args.subs and has_subs:
        fparts.append(f"[0:v]subtitles={srt.as_posix()}:force_style='FontSize=22,Outline=2'[vout]")
        vmap = "[vout]"

    out = final / f"{slug}.mp4"
    run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fparts),
         "-map", vmap, "-map", "[aout]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(out)])

    if args.vertical and ar != "9:16":
        vw, vh = RES["9:16"].get(res, (1080, 1920))
        run(["ffmpeg", "-y", "-i", str(out), "-vf",
             f"scale=-2:{vh},crop={vw}:{vh},setsar=1", "-pix_fmt", "yuv420p", "-c:a", "copy", str(final / f"{slug}_9x16.mp4")])

    print(f"\nFinal: {out} ({probe_duration(out):.1f} sn, {w}x{h})")


if __name__ == "__main__":
    main()
