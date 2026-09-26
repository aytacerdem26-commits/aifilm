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
| 4. Anahtar kareler | `goruntu-uretici` | `keyframe_url` alanları |
| 5. Hareket | `animator` | `clip_url` alanları |
| 6. Ses | `ses-tasarimcisi` | `04_ses_plani.md`, `audio/` |
| 7. Kalite kontrol | `sureklilik-denetcisi` | `05_denetim.md` (4, 5 ve 8'den sonra çalışır) |
| 8. Kurgu | `kurgucu` | `final/<slug>.mp4` |

## Kurallar

- Her proje `projects/<slug>/` altında yaşar; tek doğruluk kaynağı `03_cekim_listesi.json`'dır.
- Üretim (Nim) kredisi harcayan her adımdan önce yapımcı kullanıcıya tahmini maliyeti söyler ve onay alır.
- Model prompt'ları **İngilizce**, ekip içi dokümanlar **Türkçe** yazılır.
- Karakter tutarlılığı için her karakter/mekân önce referans görseli ile sabitlenir; sonraki
  bütün üretimler bu referansları `fileInputs` olarak kullanır.
- Agent'lar yalnızca kendi dosyalarını yazar; çekim listesindeki kendi alanlarını günceller.
- `status.md` her aşama sonunda güncellenir (proje nerede kaldı, neler onaylandı).
