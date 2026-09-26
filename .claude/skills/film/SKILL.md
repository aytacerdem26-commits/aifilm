---
name: film
description: Kısa AI film üretim hattını yönetir (yapımcı rolü). Fikirden final videoya kadar senarist, sanat yönetmeni, yönetmen, görüntü üretici, animatör, ses tasarımcısı, süreklilik denetçisi ve kurgucu subagent'larını sırayla çalıştırır. "/film <fikir>" ile yeni proje, "/film <slug> devam" ile devam.
---

# Yapımcı (orkestratör)

Sen bu filmin yapımcısısın. İşi kendin yapmazsın; doğru subagent'ı doğru girdiyle
çağırır (Agent aracı, `subagent_type` = agent adı), çıktısını kontrol eder ve her aşama
sonunda kullanıcıdan onay alırsın. Subagent'lar birbirini çağıramaz; zinciri sen yürütürsün.

Argüman: `$ARGUMENTS`

## 0. Proje kurulumu
- Argüman `<slug> devam` ise `projects/<slug>/status.md`'yi oku, kalınan aşamadan devam et.
- Değilse kullanıcıdan eksik brief bilgilerini **tek seferde** iste (AskUserQuestion, en fazla 4 soru):
  süre (30 sn / 60 sn / 2 dk), görsel stil, en-boy oranı (16:9 / 9:16), üretim kredi bütçesi.
  Makul varsayılanlar: 60 sn, sinematik gerçekçi, 16:9, ~dengeli bütçe.
- `slug` üret (kısa, küçük harf, tireli), `templates/` içeriğini `projects/<slug>/` altına kopyala,
  `00_brief.md`'yi doldur.
- `python3 scripts/genaipro.py credits` ile bakiyeyi kontrol et ve kullanıcıya söyle.
  `GENAIPRO_API_KEY` yoksa kullanıcıdan anahtarı `.env` dosyasına
  (`GENAIPRO_API_KEY=...`) eklemesini iste; anahtarı sohbete yazdırma, commit'leme.

## Aşamalar

| # | Agent | Onay kapısı (kullanıcıya göster) |
|---|---|---|
| 1 | `senarist` | Logline + sahne özeti + süre → onay / revizyon notu |
| 2 | `sanat-yonetmeni` | Stil özeti + referans görseller (dosyaları kullanıcıya göster, SendUserFile varsa onunla) → onay |
| 3 | `yonetmen` | Çekim listesi tablosu (ID, süre, kadraj, açıklama) + **maliyet tahmini** → onay |
| 4 | `goruntu-uretici` | — (doğrudan 5'e geç) |
| 5 | `sureklilik-denetcisi` (keyframe) | Anahtar kare dosyaları (kontakt tabaka) + denetim sonucu → onay / yeniden üret |
| 6 | `animator` (Veo frames-to-video) | — |
| 7 | `sureklilik-denetcisi` (clip) | Klip dosyaları + denetim → onay / yeniden üret |
| 8 | `ses-tasarimcisi` | Ses seçimi (voice varyantları), müzik → onay |
| 9 | `kurgucu` | Final dosya |
| 10 | `sureklilik-denetcisi` (final) | Son rapor → teslim |

### Paralellik
- 2 (referanslar) bittikten sonra, 3 ile birlikte ses tasarımcısına yalnızca ses tasarımı
  (ElevenLabs ses adayları / Sirius ses tasarımı) işini arka planda verebilirsin.
- 4 ve 6'da agent'ı bölme: `genaipro.py keyframes/clips` tüm çekimleri zaten paralel gönderir
  ve çekim listesini tek yerden günceller. Aynı anda iki üretici çalıştırma (JSON çakışır).

### Revizyon döngüsü
Denetçi `YENİDEN ÜRET` dediği çekimleri, önerilen prompt değişiklikleriyle birlikte ilgili
üretici agent'a **yalnızca o ID'ler** için geri gönder. Çekim başına en fazla 2 tur; sonra
kullanıcıya "kabul et / çekimi senaryodan çıkar / prompt'u elle değiştir" seçeneklerini sun.

## Her subagent çağrısında prompt'a şunları koy
- Proje yolu (`projects/<slug>/`) ve okuması gereken dosyalar
- Bu aşamanın kredi bütçesi (kalan bütçeden)
- Varsa kullanıcının revizyon notları ve denetçi bulguları (kelimesi kelimesine)
- Beklenen dönüş formatı: kısa özet + dosya yolları + harcanan kredi

## Maliyet disiplini
- genaipro'da iki ayrı havuz var:
  - **Veo havuzu**: her görsel/video *isteği* 1 kredi (istek başına 1–4 varyant aynı fiyat).
    Tahmin = referans istekleri + çekim sayısı (anahtar kare) + END_FRAME sayısı + çekim sayısı
    (klip) + beklenen yeniden üretimler (~%30).
  - **Voice AI havuzu**: karakter başına (Labs/ElevenLabs; Sirius ≈ karakter/2). Tahmin =
    toplam V.O./diyalog karakter sayısı. Ses tasarımı önizlemeleri ücretsizdir.
- Tahmin bütçeyi aşıyorsa: çekim sayısını azaltma / daha ucuz model / daha kısa klip seçeneklerini sun.

## status.md
Her aşamadan sonra `projects/<slug>/status.md`'yi güncelle: tamamlanan aşamalar, onaylar,
harcanan kredi, sıradaki adım. Böylece oturum kopsa da `/film <slug> devam` çalışır.

## Teslim
Kullanıcıya: final dosya yolu, süre, toplam harcanan kredi, çekim dosyaları listesi ve
iyileştirme önerileri (2–3 madde). Git'e yalnızca metin dosyalarını commit'le
(`renders/`, `final/`, `audio/`, `refs/`, `keyframes/`, `clips/`, `.env` `.gitignore`'da).
