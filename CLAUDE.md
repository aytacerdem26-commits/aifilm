# aifilm — Kısa AI Film Üretim Hattı

Bu repo, kısa (30 sn – 3 dk) AI filmleri uçtan uca üretmek için Claude Code
subagent'larından oluşan bir "film ekibi" içerir. Ana oturum **yapımcı** rolündedir:
ekibi sırayla çalıştırır, her aşamanın sonunda kullanıcıdan onay alır.

## Başlatma

`/film <fikir>` — yeni proje açar ve hattı baştan çalıştırır.
`/film <proje-slug> devam` — yarım kalan projeyi `projects/<slug>/status.md`'den devam ettirir.

## Ekip (`.claude/agents/`)

| Aşama | Agent | Çıktı |
|---|---|---|
| 1. Hikâye | `senarist` | `01_senaryo.md` |
| 2. Görsel dil | `sanat-yonetmeni` | `02_stil_rehberi.md`, `refs/` (karakter/mekân referansları) |
| 3. Çekim planı | `yonetmen` | `03_cekim_listesi.json` |
| 4. Anahtar kareler | `goruntu-uretici` | `keyframes/`, `keyframe_file` alanları |
| 5. Hareket | `animator` | `clips/`, `clip_file` alanları |
| 6. Ses | `ses-tasarimcisi` | `04_ses_plani.md`, `audio/` |
| 7. Kalite kontrol | `sureklilik-denetcisi` | `05_denetim.md` (4, 5 ve 8'den sonra çalışır) |
| 8. Kurgu | `kurgucu` | `final/<slug>.mp4` |

## Kurallar

- Her proje `projects/<slug>/` altında yaşar; tek doğruluk kaynağı `03_cekim_listesi.json`'dır.
- Tüm AI üretimi **genaipro.io** üzerinden, yalnızca `scripts/genaipro.py` ile yapılır
  (görsel: Nano Banana Pro/Imagen 4, video: Veo frames-to-video, ses: ElevenLabs Labs / Sirius).
  API anahtarı `GENAIPRO_API_KEY` ortam değişkeninde ya da `.env`'de; asla commit'lenmez.
- Kredi harcayan her adımdan önce yapımcı kullanıcıya tahmini maliyeti söyler ve onay alır
  (Veo havuzu: görsel/video isteği başına 1 kredi; Voice AI havuzu: karakter başına).
- Model prompt'ları **İngilizce**, ekip içi dokümanlar **Türkçe** yazılır.
- Karakter tutarlılığı için her karakter/mekân önce referans görseli ile sabitlenir; sonraki
  bütün üretimler bu referansları (`refs` alanı → `reference_images`) kullanır.
- Agent'lar yalnızca kendi dosyalarını yazar; çekim listesindeki kendi alanlarını günceller.
- `status.md` her aşama sonunda güncellenir (proje nerede kaldı, neler onaylandı).
