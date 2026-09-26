# aifilm — Subagent'lardan oluşan kısa AI film ekibi

Claude Code içinde çalışan, fikirden final `.mp4`'e kadar kısa film üreten bir yapım ekibi.

```
            /film <fikir>   (yapımcı = ana oturum, .claude/skills/film)
                  │
   ┌──────────────┼───────────────────────────────────────────────┐
   ▼              ▼              ▼                                 │
senarist → sanat-yonetmeni → yonetmen ──► goruntu-uretici ──► animator ──► ses-tasarimcisi ──► kurgucu
 senaryo    stil rehberi     çekim listesi   anahtar kareler    klipler     ses/lipsync/müzik   final.mp4
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
| `sanat-yonetmeni` | Stil rehberi, CHAR_/LOC_ tarif blokları, referans görseller | Nim görsel |
| `yonetmen` | Çekim listesi, kadraj, kamera, İngilizce prompt'lar | Dosya |
| `goruntu-uretici` | Çekim başına anahtar kare | Nim görsel |
| `animator` | Image-to-video klipler | Nim video |
| `ses-tasarimcisi` | Ses tasarımı, lipsync, V.O., müzik planı | Nim ses/lipsync |
| `sureklilik-denetcisi` | Tutarlılık & artefakt kontrolü, yeniden üretim kararı | Görüntü inceleme |
| `kurgucu` | Birleştirme, geçişler, ses miksi, altyazı, 9:16 | ffmpeg |

## Kullanım

```text
/film Yaşlı bir deniz feneri bekçisi, son gece nöbetinde denizden gelen bir ışık görür
/film deniz-feneri devam
```

Tek bir ekip üyesini de doğrudan çağırabilirsin: *"yonetmen agent'ı ile deniz-feneri
projesinin S04–S06 çekimlerini yeniden planla"*.

## Proje klasörü

```
projects/<slug>/
  00_brief.md            fikir, süre, stil, bütçe
  01_senaryo.md          senarist
  02_stil_rehberi.md     sanat yönetmeni (+ referans URL'leri)
  03_cekim_listesi.json  yönetmen; üreticiler keyframe_url / clip_url / status alanlarını doldurur
  04_ses_plani.md        ses tasarımcısı
  05_denetim.md          süreklilik denetçisi
  status.md              yapımcının ilerleme kaydı
  audio/ refs/ renders/ final/ qa/   (git'e girmez)
```

Çekim durumu akışı: `planned → keyframe_done → keyframe_approved → clip_done → clip_approved`
(başarısızlar `*_failed`, filmden çıkarılanlar `cut`).

## Gereksinimler

- Claude Code (proje klasöründe açılınca `.claude/agents` ve `/film` otomatik yüklenir)
- **Nim** MCP bağlantısı (görsel, video, ses örneği, lipsync üretimi) ve yeterli kredi
- `ffmpeg` + `ffprobe`, `python3` (kurgu için)

Kurguyu elle çalıştırmak:

```bash
python3 scripts/assemble.py projects/<slug> [--subs] [--vertical] [--no-music]
```

`audio/vo_<ÇEKİM_ID>.mp3` dosyaları o çekimin başına, `audio/music.mp3` ise tüm filmin altına
(-12 dB civarı, fade in/out) yerleştirilir.
