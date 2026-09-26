# aifilm — Subagent'lardan oluşan kısa AI film ekibi

Claude Code içinde çalışan, fikirden final `.mp4`'e kadar kısa film üreten bir yapım ekibi.

```
            /film <fikir>   (yapımcı = ana oturum, .claude/skills/film)
                  │
   ┌──────────────┼───────────────────────────────────────────────┐
   ▼              ▼              ▼                                 │
senarist → sanat-yonetmeni → yonetmen ──► goruntu-uretici ──► animator ──► ses-tasarimcisi ──► kurgucu
 senaryo    stil rehberi     çekim listesi   anahtar kareler    klipler     V.O./ses/müzik      final.mp4
            + referanslar    (JSON)              │                 │                              │
                                                 └──► sureklilik-denetcisi ◄──┘◄──────────────────┘
                                                      (onay / yeniden üret)
```

Her ok arasında yapımcı sana özet gösterir ve onay ister; kredi harcayan adımlardan önce
maliyet tahmini verir.

## Ekip

| Agent | Rol | Araçlar |
|---|---|---|
| `senarist` | Logline, karakterler, AI'a uygun senaryo | Dosya |
| `sanat-yonetmeni` | Stil rehberi, CHAR_/LOC_ tarif blokları, referans görseller | genaipro görsel (Nano Banana Pro) |
| `yonetmen` | Çekim listesi, kadraj, kamera, İngilizce prompt'lar | Dosya |
| `goruntu-uretici` | Çekim başına anahtar kare (referanslı) | genaipro görsel |
| `animator` | Anahtar kareden klip | genaipro Veo frames-to-video |
| `ses-tasarimcisi` | Ses seçimi/tasarımı, V.O., müzik planı | genaipro ElevenLabs / Sirius TTS |
| `sureklilik-denetcisi` | Tutarlılık & artefakt kontrolü, yeniden üretim kararı | Görüntü inceleme |
| `kurgucu` | Birleştirme, geçişler, ses miksi, altyazı, 9:16 | ffmpeg |

## Kullanım

```text
/film Yaşlı bir deniz feneri bekçisi, son gece nöbetinde denizden gelen bir ışık görür
/film deniz-feneri devam
```

Tek bir ekip üyesini de doğrudan çağırabilirsin: *"yonetmen agent'ı ile deniz-feneri
projesinin S04–S06 çekimlerini yeniden planla"*.

## genaipro istemcisi

Tüm üretim `scripts/genaipro.py` üzerinden (yalnızca Python standart kütüphanesi):

```bash
python3 scripts/genaipro.py credits
python3 scripts/genaipro.py image --prompt "..." --ref refs/elif.png --n 4 --out refs/elif.png
python3 scripts/genaipro.py keyframes projects/<slug> --variants 2   # tüm çekimler, JSON'u günceller
python3 scripts/genaipro.py clips projects/<slug>                    # Veo frames-to-video
python3 scripts/genaipro.py voices --language tr --gender female
python3 scripts/genaipro.py tts --voice-id <id> --text "..." --out audio/vo_S01.mp3
```

Sınırlar: Veo yalnızca 16:9 / 9:16, klip ~8 sn (kurguda kırpılır), ayrı dudak senkronu ve müzik
üretimi yok. Diyaloglar Veo'ya klip içinde ürettirilir ya da V.O. olarak seslendirilir;
müzik `audio/music.mp3` olarak eklenir.

## Proje klasörü

```
projects/<slug>/
  00_brief.md            fikir, süre, stil, bütçe
  01_senaryo.md          senarist
  02_stil_rehberi.md     sanat yönetmeni (+ refs/ referans dosyaları)
  03_cekim_listesi.json  yönetmen; üreticiler keyframe_file / clip_file / status alanlarını doldurur
  04_ses_plani.md        ses tasarımcısı
  05_denetim.md          süreklilik denetçisi
  status.md              yapımcının ilerleme kaydı
  refs/ keyframes/ clips/ audio/ renders/ final/ qa/   (git'e girmez)
```

Çekim durumu akışı: `planned → keyframe_done → keyframe_approved → clip_done → clip_approved`
(başarısızlar `*_failed`, filmden çıkarılanlar `cut`).

## Gereksinimler

- Claude Code (proje klasöründe açılınca `.claude/agents` ve `/film` otomatik yüklenir)
- **genaipro.io** hesabı ve API anahtarı (avatar → Manage Account → API Key).
  `.env.example`'ı `.env` olarak kopyalayıp `GENAIPRO_API_KEY=...` yaz (`.env` git'e girmez).
  Veo kredisi (görsel/video: istek başına 1) ve Voice AI kredisi (TTS: karakter başına) gerekir.
- `ffmpeg` + `ffprobe`, `python3` (kurgu için)

Kurguyu elle çalıştırmak:

```bash
python3 scripts/assemble.py projects/<slug> [--subs] [--vertical] [--no-music]
```

`audio/vo_<ÇEKİM_ID>.mp3` dosyaları o çekimin başına, `audio/music.mp3` ise tüm filmin altına
(-12 dB civarı, fade in/out) yerleştirilir. Her klibin kendi (Veo) sesi `clip_volume` ile ayarlanır.
