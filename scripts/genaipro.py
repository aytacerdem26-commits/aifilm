#!/usr/bin/env python3
"""genaipro.io istemcisi — film hattının tüm üretim çağrıları buradan geçer.

API anahtarı: GENAIPRO_API_KEY ortam değişkeni ya da repo kökündeki .env dosyası.
(genaipro.io → avatar → Manage Account → API Key)

Tekil komutlar (sonucu indirir, JSON özet basar):
  credits                                           Veo + Voice AI kredi durumu
  fetch TASK_ID --out x.png                         Tamamlanmış görevi yeniden indir (kredisiz)
  image  --prompt P [--ref a.png ...] --out x.png   Görsel (Nano Banana Pro / Imagen / GPT)
  video  --start k.png [--end e.png] --prompt P --out x.mp4    Veo frames-to-video
  ingredients --ref a.png [...] --prompt P --out x.mp4         Veo, referanslardan video
  video/ingredients ... --omni [--omni-duration 4|6|8|10] [--omni-resolution 720p]
                                                    Omni 1.1 (omni_flash), video başına ücretli
  voices [--search S] [--language tr] [--gender female]        ElevenLabs ses kataloğu
  voice-design --instructions "..."                 Sirius ses tasarımı önizlemesi (ücretsiz)
  voice-design-save ID --name AD                    Önizlemeyi kaydet → voice_design_id
  tts --engine labs --voice-id V --text T --out x.mp3
  tts --engine sirius (--voice V | --voice-design-id D) [--style S] --text T --out x.mp3

Çekim listesi üzerinde toplu komutlar (03_cekim_listesi.json'ı günceller):
  keyframes projects/<slug> [--ids S01,S02] [--variants 2]
  clips     projects/<slug> [--ids S01,S02] [--variants 2]
"""
import argparse
import http.client
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

BASE = os.environ.get("GENAIPRO_BASE_URL", "https://genaipro.io/api")
ROOT = Path(__file__).resolve().parent.parent
# urllib'in varsayılan "Python-urllib/x.y" kimliği yerine istemciyi açıkça tanıtan User-Agent
USER_AGENT = "aifilm-genaipro-client/1.0 (+https://github.com/aytacerdem26-commits/aifilm)"

IMAGE_AR = {
    "16:9": "IMAGE_ASPECT_RATIO_LANDSCAPE",
    "4:3": "IMAGE_ASPECT_RATIO_LANDSCAPE_FOUR_THREE",
    "1:1": "IMAGE_ASPECT_RATIO_SQUARE",
    "3:4": "IMAGE_ASPECT_RATIO_PORTRAIT_THREE_FOUR",
    "9:16": "IMAGE_ASPECT_RATIO_PORTRAIT",
}
VIDEO_AR = {"16:9": "VIDEO_ASPECT_RATIO_LANDSCAPE", "9:16": "VIDEO_ASPECT_RATIO_PORTRAIT"}

# Omni 1.1 (model=omni_flash): aynı Veo uç noktalarında; süre ve çözünürlük seçilebilir, sesli.
# Fiyat video başına (genaipro.io site tablosu / /api/config OMNI_GOOGLE_RATIO, 2026-10 itibarıyla 4).
OMNI_DURATIONS = (4, 6, 8, 10)
OMNI_RESOLUTIONS = ("360p", "720p", "1080p")
OMNI_PRICE_TABLE = {"360p": {4: 4, 6: 5, 8: 6, 10: 7}, "720p": {4: 7, 6: 10, 8: 12, 10: 15},
                    "1080p": {4: 7, 6: 10, 8: 12, 10: 15}}


# ─── HTTP ───────────────────────────────────────────────────────────────────

def api_key():
    key = os.environ.get("GENAIPRO_API_KEY")
    if not key:
        env = ROOT / ".env"
        if env.exists():
            for line in env.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("GENAIPRO_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip("'\"")
    if not key:
        sys.exit("GENAIPRO_API_KEY yok: ortam değişkeni olarak ya da .env dosyasına ekleyin.")
    return key


def multipart(fields, files):
    """fields: [(ad, değer)], files: [(ad, yol)] → (gövde, content-type)."""
    boundary = uuid.uuid4().hex
    out = bytearray()
    for name, value in fields:
        out += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n"
                f"{value}\r\n").encode()
    for name, path in files:
        path = Path(path)
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        out += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; "
                f"filename=\"{path.name}\"\r\nContent-Type: {ctype}\r\n\r\n").encode()
        out += path.read_bytes() + b"\r\n"
    out += f"--{boundary}--\r\n".encode()
    return bytes(out), f"multipart/form-data; boundary={boundary}"


def request(method, path, *, json_body=None, fields=None, files=None, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    headers = {"Authorization": f"Bearer {api_key()}", "Accept": "application/json",
               "User-Agent": USER_AGENT}
    data = None
    if json_body is not None:
        data = json.dumps(json_body).encode()
        headers["Content-Type"] = "application/json"
    elif fields is not None or files:
        data, headers["Content-Type"] = multipart(fields or [], files or [])
    for attempt in range(6):
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as e:
            text = e.read().decode(errors="replace")
            if e.code == 429 or e.code >= 500:
                wait = 2 ** attempt * 5
                reset = e.headers.get("X-RateLimit-Reset", "")
                if reset.isdigit():  # epoch saniye ya da kalan saniye olabilir
                    wait = int(reset) - int(time.time()) if int(reset) > 1e9 else int(reset)
                print(f"  HTTP {e.code}, {wait}s sonra tekrar denenecek…", file=sys.stderr)
                time.sleep(min(max(wait, 1), 90))
                continue
            sys.exit(f"genaipro {method} {path} → HTTP {e.code}: {text}")
        except (urllib.error.URLError, http.client.HTTPException, ConnectionError, TimeoutError) as e:
            print(f"  bağlantı hatası ({e}), tekrar deneniyor…", file=sys.stderr)
            time.sleep(2 ** attempt * 2)
    sys.exit(f"genaipro {method} {path}: tekrar denemeler tükendi")


def download(url, dest):
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        r = urllib.request.urlopen(req, timeout=300)
    except urllib.error.HTTPError as e:
        if e.code not in (401, 403):
            raise
        req.add_header("Authorization", f"Bearer {api_key()}")
        r = urllib.request.urlopen(req, timeout=300)
    with r, open(dest, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    return dest


# ─── Görev takibi ───────────────────────────────────────────────────────────

def wait_tasks(ids, kind="veo", interval=15, timeout=1800):
    """Veo / gt-mage görevlerini tamamlanana kadar bekler. {id: görev} döndürür.

    Tek istekte hepsini görmek için histories uç noktasını kullanır (30 istek/dk limiti).
    """
    pending, done = set(ids), {}
    start = time.time()
    while pending:
        if time.time() - start > timeout:
            for i in pending:
                done[i] = {"id": i, "status": "failed", "error": "zaman aşımı", "file_urls": []}
            break
        if len(pending) == 1:
            items = [request("GET", f"/v2/{kind}/tasks/{next(iter(pending))}")]
        else:
            items = request("GET", f"/v2/{kind}/histories", params={"page": 1, "page_size": 100}).get("data", [])
            seen = {t.get("id") for t in items}
            # histories'in ilk sayfasında görünmeyen görevleri tek tek sor
            items += [request("GET", f"/v2/{kind}/tasks/{tid}") for tid in list(pending - seen)[:5]]
        for t in items:
            if t.get("id") in pending and t.get("status") in ("completed", "failed"):
                done[t["id"]] = t
                pending.discard(t["id"])
                print(f"  {t['id'][:8]} → {t['status']}", file=sys.stderr)
        if pending:
            time.sleep(interval)
    return done


def task_id(resp):
    """Oluşturma yanıtından görev ID'si (video: histories[0].id, görsel: id)."""
    if "histories" in resp:
        return resp["histories"][0]["id"]
    return resp["id"]


# ─── Üretim çağrıları ───────────────────────────────────────────────────────

def submit_image(prompt, refs=(), aspect="16:9", n=1, model="nano_banana_pro", engine="veo", upscale=""):
    if engine == "gpt":
        fields = [("prompt", prompt), ("size", aspect), ("n", str(n))]
        return task_id(request("POST", "/v2/gt-mage/create-image", fields=fields,
                               files=[("reference_images", r) for r in refs[:3]])), "gt-mage"
    fields = [("prompt", prompt), ("aspect_ratio", IMAGE_AR[aspect]),
              ("number_of_images", str(n)), ("model", model)]
    if upscale:
        fields.append(("upscale_resolution", upscale))
    return task_id(request("POST", "/v2/veo/create-image", fields=fields,
                           files=[("reference_images", r) for r in refs[:5]])), "veo"


def omni_duration(seconds):
    """İstenen süreyi kapsayan en kısa Omni süresi (4/6/8/10)."""
    return next((d for d in OMNI_DURATIONS if d >= seconds), OMNI_DURATIONS[-1])


def omni_cost(duration, resolution, n=1, ratio=4):
    return max(1, OMNI_PRICE_TABLE[resolution][duration] // ratio) * n


def video_fields(prompt, aspect, n, upscale, omni):
    """omni: None (Veo, istek başına 1 kredi) ya da {"duration": 4-10, "resolution": "720p"}."""
    fields = [("prompt", prompt), ("aspect_ratio", VIDEO_AR[aspect]), ("number_of_videos", str(n))]
    if omni:
        fields += [("model", "omni_flash"), ("duration", str(omni["duration"])),
                   ("resolution", omni.get("resolution", "720p"))]
    elif upscale:
        fields.append(("upscale_resolution", upscale))
    return fields


def submit_video(prompt, start, end=None, aspect="16:9", n=1, upscale="", omni=None):
    fields = video_fields(prompt, aspect, n, upscale, omni)
    files = [("start_image", start)] + ([("end_image", end)] if end else [])
    return task_id(request("POST", "/v2/veo/frames-to-video", fields=fields, files=files))


def submit_ingredients(prompt, refs, aspect="16:9", n=1, upscale="", omni=None):
    fields = video_fields(prompt, aspect, n, upscale, omni)
    return task_id(request("POST", "/v2/veo/ingredients-to-video", fields=fields,
                           files=[("reference_images", r) for r in refs[:3]]))


def log_task(task, out):
    """Tamamlanan görevi indirmeden önce kaydeder; indirme düşerse `fetch` ile kurtarılır."""
    log = Path(out).parent / "genaipro_tasks.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    with open(log, "a", encoding="utf-8") as f:
        f.write(json.dumps({"task_id": task.get("id"), "out": str(out),
                            "file_urls": task.get("file_urls") or []}, ensure_ascii=False) + "\n")
    print(f"  görev {task.get('id')} → {log}", file=sys.stderr)


def save_outputs(task, out):
    """Görev çıktılarını indirir: tek dosya → out, birden çok → out_v1, out_v2…"""
    out = Path(out)
    urls = task.get("file_urls") or []
    log_task(task, out)
    paths = []
    for i, url in enumerate(urls, 1):
        dest = out if len(urls) == 1 else out.with_name(f"{out.stem}_v{i}{out.suffix}")
        paths.append(str(download(url, dest)))
    return paths


def emit(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


# ─── Tekil komutlar ─────────────────────────────────────────────────────────

def cmd_fetch(a):
    """Tamamlanmış bir görevin çıktılarını yeniden indirir (kredi harcamaz)."""
    kind = "gt-mage" if a.gpt else "veo"
    t = request("GET", f"/v2/{kind}/tasks/{a.task_id}")
    if t.get("status") != "completed":
        sys.exit(f"görev durumu: {t.get('status')} {t.get('error', '')}")
    emit({"task_id": a.task_id, "file_urls": t.get("file_urls", []), "files": save_outputs(t, a.out)})


def cmd_credits(a):
    emit({"user": request("GET", "/v2/me"),
          "veo_credits": request("GET", "/v2/veo/credits"),
          "voice_credits": request("GET", "/v1/labs/credits")})


def cmd_image(a):
    tid, kind = submit_image(a.prompt, a.ref, a.aspect, a.n, a.model, a.engine, a.upscale)
    t = wait_tasks([tid], kind, interval=5)[tid]
    emit({"task_id": tid, "status": t["status"], "error": t.get("error"),
          "file_urls": t.get("file_urls", []),
          "files": save_outputs(t, a.out) if t["status"] == "completed" else []})


def cli_omni(a):
    if not a.omni:
        return None
    print(f"  Omni: {a.omni_duration} sn {a.omni_resolution}, tahmini "
          f"{omni_cost(a.omni_duration, a.omni_resolution, a.n)} kredi", file=sys.stderr)
    return {"duration": a.omni_duration, "resolution": a.omni_resolution}


def cmd_video(a):
    tid = submit_video(a.prompt, a.start, a.end, a.aspect, a.n, a.upscale, cli_omni(a))
    t = wait_tasks([tid])[tid]
    emit({"task_id": tid, "status": t["status"], "error": t.get("error"),
          "file_urls": t.get("file_urls", []),
          "files": save_outputs(t, a.out) if t["status"] == "completed" else []})


def cmd_ingredients(a):
    tid = submit_ingredients(a.prompt, a.ref, a.aspect, a.n, a.upscale, cli_omni(a))
    t = wait_tasks([tid])[tid]
    emit({"task_id": tid, "status": t["status"], "error": t.get("error"),
          "file_urls": t.get("file_urls", []),
          "files": save_outputs(t, a.out) if t["status"] == "completed" else []})


def cmd_voices(a):
    voices = request("GET", "/v1/labs/voices", params={
        "search": a.search, "language": a.language, "gender": a.gender, "age": a.age,
        "accent": a.accent, "use_cases": a.use_case, "page_size": a.limit})
    emit([{k: v.get(k) for k in ("voice_id", "name", "gender", "age", "accent", "language",
                                 "descriptive", "use_case", "preview_url")} for v in voices])


def cmd_voice_design(a):
    body = {"instructions": a.instructions}
    if a.seed:
        body["seed"] = a.seed
    d = request("POST", "/v1/tts/sirius/voice-designs", json_body=body)
    did = d.get("id")
    while d.get("status") not in ("done", "failed"):
        time.sleep(5)
        d = request("GET", f"/v1/tts/sirius/voice-designs/{did}")
    if a.out and d.get("preview_url"):
        d["file"] = str(download(d["preview_url"], a.out))
    emit(d)


def cmd_voice_design_save(a):
    emit(request("POST", f"/v1/tts/sirius/voice-designs/{a.id}/save",
                  json_body={"title": a.name}))


def cmd_tts(a):
    if a.engine == "labs":
        body = {"input": a.text, "voice_id": a.voice_id, "model_id": a.model,
                "speed": a.speed, "stability": a.stability}
        tid = request("POST", "/v1/labs/task", json_body=body)["task_id"]
        path = f"/v1/labs/task/{tid}"
    else:
        body = {"content": a.text}
        if a.voice_design_id:
            body["voice_design_id"] = a.voice_design_id
        else:
            body["voice"] = a.voice
            if a.style:
                body["style"] = a.style
        tid = request("POST", "/v1/tts/sirius", json_body=body)["id"]
        path = f"/v1/tts/sirius/{tid}"
    while True:
        t = request("GET", path)
        if t.get("status") in ("completed", "failed"):
            break
        time.sleep(3)
    res = {"task_id": tid, "status": t["status"], "error": t.get("error"), "result": t.get("result")}
    if t["status"] == "completed" and t.get("result"):
        res["file"] = str(download(t["result"], a.out))
    emit(res)


# ─── Çekim listesi üzerinde toplu işler ─────────────────────────────────────

def load_shotlist(project):
    p = Path(project) / "03_cekim_listesi.json"
    return p, json.loads(p.read_text(encoding="utf-8"))


def save_shotlist(p, data):
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(p)


def select(shots, ids, statuses):
    if ids:
        want = set(ids.split(","))
        return [s for s in shots if s["id"] in want]
    return [s for s in shots if s.get("status") in statuses]


def batch(project, shots, submit, kind, out_dir, ext, url_field, file_field, ok_status, fail_status):
    """Görevleri 25'lik dalgalarla gönderir (dakikada 30 istek sınırı), bekler, indirir."""
    p, data = project
    proj = p.parent
    by_id = {s["id"]: s for s in data["shots"]}
    report = []
    for i in range(0, len(shots), 25):
        wave = shots[i:i + 25]
        jobs = {}
        for s in wave:
            tid = submit(s)
            jobs[tid] = s["id"]
            print(f"{s['id']}: görev {tid}", file=sys.stderr)
        results = wait_tasks(list(jobs), kind, interval=15 if ext == "mp4" else 8)
        for tid, t in results.items():
            s = by_id[jobs[tid]]
            if t["status"] == "completed" and t.get("file_urls"):
                files = save_outputs(t, proj / out_dir / f"{s['id']}.{ext}")
                rel = [str(Path(f).relative_to(proj)) for f in files]
                s[file_field] = rel[0]
                s[url_field] = t["file_urls"][0]
                if len(rel) > 1:
                    s[f"{file_field}_variants"] = rel
                s["status"] = ok_status
            else:
                s["status"] = fail_status
                s["notes"] = (s.get("notes", "") + f" [{fail_status}: {t.get('error', '')}]").strip()
            report.append({"id": s["id"], "status": s["status"], "files": s.get(f"{file_field}_variants")
                           or [s.get(file_field)], "error": t.get("error")})
        save_shotlist(p, data)
    emit(report)


def cmd_keyframes(a):
    p, data = load_shotlist(a.project)
    proj = p.parent
    ar = data.get("aspect_ratio", "16:9")
    shots = select(data["shots"], a.ids, {"planned", "keyframe_failed"})

    def submit(s):
        refs = [proj / r for r in s.get("refs", [])]
        missing = [str(r) for r in refs if not r.exists()]
        if missing:
            sys.exit(f"{s['id']}: referans dosyası yok: {missing}")
        tid, _ = submit_image(s["image_prompt"], refs, ar, a.variants, a.model)
        return tid

    batch((p, data), shots, submit, "veo", "keyframes", "png",
          "keyframe_url", "keyframe_file", "keyframe_done", "keyframe_failed")


def cmd_clips(a):
    p, data = load_shotlist(a.project)
    proj = p.parent
    ar = data.get("aspect_ratio", "16:9")
    if ar not in VIDEO_AR:
        sys.exit(f"Veo yalnızca 16:9 ve 9:16 destekler (liste: {ar})")
    shots = select(data["shots"], a.ids, {"keyframe_approved", "clip_failed"})
    upscale = "1080p" if data.get("resolution") == "1080p" else ""

    res = data.get("resolution", "720p") if data.get("resolution") in OMNI_RESOLUTIONS else "720p"

    def shot_omni(s):
        # --omni hepsini, çekimdeki "video_model": "omni" yalnız o çekimi Omni ile üretir
        if not (a.omni or s.get("video_model") == "omni"):
            return None
        d = s.get("omni_duration") or omni_duration(float(s.get("duration_s", 8)))
        return {"duration": int(d), "resolution": res}

    total = sum(omni_cost(o["duration"], o["resolution"], a.variants) if (o := shot_omni(s)) else 1
                for s in shots)
    print(f"{len(shots)} çekim, tahmini {total} Veo kredisi", file=sys.stderr)

    def submit(s):
        start = proj / s["keyframe_file"]
        end = proj / s["end_keyframe_file"] if s.get("end_keyframe_file") else None
        return submit_video(s["video_prompt"], start, end, ar, a.variants, upscale, shot_omni(s))

    batch((p, data), shots, submit, "veo", "clips", "mp4",
          "clip_url", "clip_file", "clip_done", "clip_failed")


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("credits").set_defaults(fn=cmd_credits)

    s = sub.add_parser("fetch", help="tamamlanmış görevi yeniden indir (kredi harcamaz)")
    s.add_argument("task_id")
    s.add_argument("--out", required=True)
    s.add_argument("--gpt", action="store_true", help="gt-mage (ChatGPT Image) görevi")
    s.set_defaults(fn=cmd_fetch)

    s = sub.add_parser("image")
    s.add_argument("--prompt", required=True)
    s.add_argument("--ref", nargs="*", default=[])
    s.add_argument("--aspect", default="16:9", choices=list(IMAGE_AR))
    s.add_argument("--n", type=int, default=1)
    s.add_argument("--model", default="nano_banana_pro", choices=["nano_banana_pro", "nano_banana_2", "imagen_4"])
    s.add_argument("--engine", default="veo", choices=["veo", "gpt"])
    s.add_argument("--upscale", default="", choices=["", "2k", "4k"])
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_image)

    s = sub.add_parser("video")
    s.add_argument("--prompt", required=True)
    s.add_argument("--start", required=True)
    s.add_argument("--end")
    s.add_argument("--aspect", default="16:9", choices=list(VIDEO_AR))
    s.add_argument("--n", type=int, default=1)
    s.add_argument("--upscale", default="", choices=["", "1080p"])
    s.add_argument("--omni", action="store_true", help="Omni 1.1 (omni_flash): süre seçilebilir, video başına ücretli")
    s.add_argument("--omni-duration", type=int, default=8, choices=OMNI_DURATIONS)
    s.add_argument("--omni-resolution", default="720p", choices=OMNI_RESOLUTIONS)
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_video)

    s = sub.add_parser("ingredients")
    s.add_argument("--prompt", required=True)
    s.add_argument("--ref", nargs="+", required=True)
    s.add_argument("--aspect", default="16:9", choices=list(VIDEO_AR))
    s.add_argument("--n", type=int, default=1)
    s.add_argument("--upscale", default="", choices=["", "1080p"])
    s.add_argument("--omni", action="store_true", help="Omni 1.1 (omni_flash): süre seçilebilir, video başına ücretli")
    s.add_argument("--omni-duration", type=int, default=8, choices=OMNI_DURATIONS)
    s.add_argument("--omni-resolution", default="720p", choices=OMNI_RESOLUTIONS)
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_ingredients)

    s = sub.add_parser("voices")
    for f in ("search", "language", "gender", "age", "accent", "use-case"):
        s.add_argument(f"--{f}")
    s.add_argument("--limit", type=int, default=20)
    s.set_defaults(fn=cmd_voices)

    s = sub.add_parser("voice-design")
    s.add_argument("--instructions", required=True)
    s.add_argument("--seed", type=int)
    s.add_argument("--out")
    s.set_defaults(fn=cmd_voice_design)

    s = sub.add_parser("voice-design-save")
    s.add_argument("id")
    s.add_argument("--name", required=True)
    s.set_defaults(fn=cmd_voice_design_save)

    s = sub.add_parser("tts")
    s.add_argument("--engine", default="labs", choices=["labs", "sirius"])
    s.add_argument("--text", required=True)
    s.add_argument("--voice-id", help="labs: /v1/labs/voices voice_id")
    s.add_argument("--model", default="eleven_multilingual_v2",
                   choices=["eleven_multilingual_v2", "eleven_turbo_v2_5", "eleven_flash_v2_5", "eleven_v3"])
    s.add_argument("--speed", type=float, default=1.0)
    s.add_argument("--stability", type=float, default=0.6)
    s.add_argument("--voice", help="sirius hazır ses")
    s.add_argument("--voice-design-id", help="sirius kayıtlı ses tasarımı")
    s.add_argument("--style", help="sirius: konuşma talimatı (yalnızca hazır seslerde)")
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_tts)

    for name, fn in (("keyframes", cmd_keyframes), ("clips", cmd_clips)):
        s = sub.add_parser(name)
        s.add_argument("project")
        s.add_argument("--ids", help="virgülle ayrılmış çekim ID'leri")
        s.add_argument("--variants", type=int, default=1, choices=[1, 2, 3, 4],
                       help="çekim başına varyant (istek başına 1 kredi, varyant sayısından bağımsız)")
        if name == "clips":
            s.add_argument("--omni", action="store_true",
                           help="tüm çekimleri Omni ile üret (yoksa yalnızca video_model=omni olanlar)")
        if name == "keyframes":
            s.add_argument("--model", default="nano_banana_pro", choices=["nano_banana_pro", "nano_banana_2", "imagen_4"])
        s.set_defaults(fn=fn)

    a = ap.parse_args()
    if a.cmd == "tts":
        if a.engine == "labs" and not a.voice_id:
            ap.error("--engine labs için --voice-id gerekli")
        if a.engine == "sirius" and not (a.voice or a.voice_design_id):
            ap.error("--engine sirius için --voice veya --voice-design-id gerekli")
    a.fn(a)


if __name__ == "__main__":
    main()
