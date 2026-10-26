# 04 — Ses Planı (V.O. üretildi: 10/10 dosya hazır, müzik bekleniyor)

**Proje:** son-nobet ("The Last Watch") · **Dil:** İngilizce V.O. · **Tek ses:** NURİ (V.O.)
**Durum:** Ses seçildi (kullanıcı: David - Raspy and Soft). 10 V.O. satırının hepsi üretildi,
ölçüldü, hepsi çekim süresine sığıyor. Sirius tasarımı kaydedilmedi (gerek kalmadı).
`audio/music.mp3` henüz yok (bkz. bölüm 3).
**Harcanan Voice AI kredisi:** 563 karakter (bakiye 995.743 → 995.180, bitiş 2026-11-18).
Ayrıntı bölüm 2'de.

---

## 0. Seçilen ses ve sabit ayarlar

| Rol | Motor | Ses | voice_id | Model | speed | stability |
|---|---|---|---|---|---|---|
| NURİ (V.O.) | Labs (ElevenLabs) | David - Raspy and Soft | `WdZjiN0nNcik2LBjOHiv` | `eleven_multilingual_v2` | 0.8 | 0.6 |

Diğer parametreler API varsayılanı: similarity 0.5, style 0, speaker_boost açık.

Yeniden üretim komutu (metin = çekim listesindeki `voiceover` alanı, birebir):
```bash
python3 scripts/genaipro.py tts --engine labs --voice-id WdZjiN0nNcik2LBjOHiv \
  --model eleven_multilingual_v2 --speed 0.8 --stability 0.6 \
  --text "<satır>" --out projects/son-nobet/audio/vo_<ÇEKİM_ID>.mp3
```

### S12 sınama turu (ayar seçimi)
Ölçüm ffmpeg ile yapıldı (süre, konuşma sonu, `silencedetect -40 dB`, ortalama ses düzeyi).
Dosyalar insan kulağıyla dinlenmedi; değerlendirme ölçüye dayanıyor.

| Deneme | Süre | Konuşma | "..." duraksaması | Ortalama düzey | Sonuç |
|---|---|---|---|---|---|
| multilingual_v2, speed 0.9, stab 0.5 | 4,44 sn | ilk bölüm 2,3 sn (~3 kelime/sn) | 1,0 sn | −18,3 dB | Fazla akıcı, "anlatıcı" temposu |
| eleven_v3, speed 0.85, stab 0.5 | 4,44 sn | ilk bölüm 2,5 sn | 0,6 + 0,3 sn | −15,1 dB | En yüksek sesli, en az fısıltılı; elenen |
| **multilingual_v2, speed 0.8, stab 0.6** | **5,25 sn** | ilk bölüm 3,0 sn (~2,3 kelime/sn) | 0,8 sn | **−23,2 dB** | **Seçildi.** Yavaş, en alçak ve yumuşak; tarife en yakın |

Elenen denemeler `audio/takes/` altında (kurgu script'i bu klasörü okumaz):
`S12_mlv2_sp090_st050.mp3`, `S12_v3_sp085_st050.mp3`.

---

## 1. Ses tablosu (aday araştırması, arşiv)

### Hedef ses profili (01_senaryo.md'den)
NURİ, 72 yaşında, Kuzey Egeli eski fener bekçisi. Ses alçak, hafif kısık, yavaş ve sakin olmalı.
Cümleler arasında nefes payı bırakır. Yaşlı ama çökmüş değil; kulağa yakın, fısıltıya yakın bir
yakınlığı var. Belirsiz bir Akdeniz aksanı olabilir ama şart değil.
Kaçınılacaklar: "trailer" bası, teatral tını, radyo sunucusu sesi, titrek/hasta yaşlı sesi.

### A) ElevenLabs (Labs) katalog adayları
Tarama: `--gender male --age old` (en ve narrative_story), ayrıca old, narrator, grandfather,
grandpa, fisherman, sailor, deep, raspy, husky, gravelly, whisper, greek, turkish, mediterranean,
italian, storyteller, elderly, wise ve "old man" aramaları yapıldı. ~320 tekil ses tarandı.
Not: Katalogda kullanım alanı değeri `narration` değil, `narrative_story`.

| # | Ad | voice_id | Özellikler (katalog) | Neden aday | preview_url |
|---|---|---|---|---|---|
| 1 | David - Raspy and Soft | `WdZjiN0nNcik2LBjOHiv` | old · british · wise · narrative_story | Kısık ama yumuşak; tarife en yakın etiket kombinasyonu | https://storage.googleapis.com/eleven-public-prod/database/workspace/a132b12665fb44298366974cbedbdf07/voices/WdZjiN0nNcik2LBjOHiv/woN3RTYTrPyPpKbjgT6d.mp3 |
| 2 | Alder - Warm, Raspy and Comforting | `nTMUXLFSfbWmdKKy7nDC` | old · irish · husky · narrative_story | Sıcak, husky, teselli edici; denizci/kıyı karakterine uygun | https://storage.googleapis.com/eleven-public-prod/database/user/qr1Waa0SQiZorbgXHZxbIe8aUxg1/voices/nTMUXLFSfbWmdKKy7nDC/I0FAhCFwCQr54oxJLr1r.mp3 |
| 3 | Michael Moody - Grandfatherly warm and deep | `PerZoH0r6nxBZXCoIPpv` | old · american · wise · narrative_story | Dede sıcaklığı, alçak; aksan Amerikan (nötr seçenek) | https://storage.googleapis.com/eleven-public-prod/database/user/ghhxYFSr6DZUXDF4V3gpvN3tGsn1/voices/PerZoH0r6nxBZXCoIPpv/HI04nJ747vsQaRlgDoeB.mp3 |
| 4 | Ezekiel - raspy narrator | `2tTjAGX0n5ajDmazDcWk` | old · american · raspy · narrative_story | Yıpranmış, çakıllı anlatıcı; fazla sert çıkabilir | https://storage.googleapis.com/eleven-public-prod/database/user/42eCmLTgIOgCLidvBqcZY0bZj9g2/voices/2tTjAGX0n5ajDmazDcWk/zjbO25LrIrs6dudzUg67.mp3 |
| 5 | Ersan - Friendly, Warm | `jSLgazTuNHl5kcEiiHgd` | old · turkish aksanlı İngilizce · confident · informative_educational | Tek yaşlı Türk aksanlı İngilizce ses (Ege rengi); eğitim tonu fazla "sunucu" olabilir | https://api.us.elevenlabs.io/v1/voices/jSLgazTuNHl5kcEiiHgd/previews/audio?payload=eyJ2b2ljZV9zb3VyY2UiOiJjdXN0b20iLCJ3b3Jrc3BhY2VfaWQiOiJhNDFiZjA3MTIxYzQ0NDUwYTY0M2RiZGFlNzBiYTg0ZSIsImZpbGVuYW1lIjoiMDc5NWY3OWUtYjdmZi00ZWZmLWIxM2MtYzM3NTFiMWQxMDYzLm1wMyIsInRpbWVzdGFtcCI6MTc5MzAzMDQwMDAwMDAwMH0%3D |
| 6 | Maximus - The Whisperer | `IxvPH8fNJQrOdR4brk0c` | old · german aksanlı · chill · narrative_story | Fısıltı yakınlığı için; Alman aksanı Ege'ye uymayabilir | https://storage.googleapis.com/eleven-public-prod/database/workspace/f6e76809451545e398253e772a7086b1/voices/IxvPH8fNJQrOdR4brk0c/C5T0MBtHO1O441nFWlM5.mp3 |
| J | Nikos - Deep and resonant (joker) | `QnPbsq4pmOZkrE4RQQCA` | old · Yunanca (el) · deep · narrative_story | Yunanca ses; multilingual_v2 ile İngilizce okutulursa doğal Yunan aksanı verebilir. Telaffuz riski var, önizleme Yunanca | https://storage.googleapis.com/eleven-public-prod/database/workspace/1da06ea679a54975ad96a2221fe6530d/voices/QnPbsq4pmOZkrE4RQQCA/736dfdd4-5ee5-44ec-8938-2bf62aa62bf5.mp3 |

`api.us.elevenlabs.io/...previews` biçimindeki bağlantılar zaman damgalı; açılmazsa
`voices --search "<ad>"` ile yenilenir.

Model: `eleven_multilingual_v2` (sakin ve tutarlı anlatım). Daha fazla nefes ve fısıltı nüansı
gerekirse `eleven_v3` ile karşılaştırılacak.

### B) Sirius ses tasarımı önizlemeleri (ücretsiz, 2 istek kullanıldı, KAYDEDİLMEDİ)

| # | preview_id | Dosya (yerel, git dışı) | Süre | Tarif özeti |
|---|---|---|---|---|
| 1 | `01a17907-9ad6-755f-823f-d1ad096de658` | audio/design_nuri_1.mp3 | 14,0 sn | 72 yaşında Kuzey Egeli bekçi; alçak, hafif kısık, fısıltıya yakın, nefesli; çok hafif belirsiz Akdeniz aksanı |
| 2 | `01a17907-b4d6-7105-ac96-91d7218426ca` | audio/design_nuri_2.mp3 | 11,6 sn | 70'lerinde; derin, çakıllı ama yumuşak; nötr İngilizce, çok hafif Rum/Türk kıyı rengi; gece sır verir gibi |

Önizleme bağlantıları:
- 1: https://files.genaipro.io/design-previews/01a17907-9ad6-755f-823f-d1ad096de658-470a37f72c7e762a.mp3
- 2: https://files.genaipro.io/design-previews/01a17907-b4d6-7105-ac96-91d7218426ca-13bcd25ccc145501.mp3

Tam tarifler:
1. "A 72-year-old man, a retired lighthouse keeper from the North Aegean. Low, slightly husky, warm voice. Speaks slowly and calmly, with soft breaths between phrases, intimate and close to the microphone, almost a whisper. Old but not frail. Very light, unplaceable Mediterranean accent in English. Gentle, melancholic, never theatrical."
2. "Elderly man in his seventies, deep and gravelly but soft, weathered by sea wind. Calm, unhurried storytelling in neutral English with only a faint Greek-Turkish coastal colouring. Quiet, close-mic intimacy, like confiding a secret at night. Steady, warm, tired but tender; no tremble, no drama."

Beğenilen tasarım şu komutla kaydedilir (onaydan sonra; hesap başına en fazla 3 tasarım):
`python3 scripts/genaipro.py voice-design-save <preview_id> --name "nuri"`

### Öneri (etiket ve tarife göre; ses dosyaları henüz insan kulağıyla dinlenmedi)
1. **Birincil: David - Raspy and Soft (`WdZjiN0nNcik2LBjOHiv`), Labs.** "Raspy + soft + wise + old"
   etiketleri tarifle birebir örtüşüyor. Katalog sesi olduğu için 10 satırda tını tutarlı kalır.
   Hafif İngiliz aksanı nötr ve belirsiz kalırsa sorun değil.
2. **Yedek: Alder (`nTMUXLFSfbWmdKKy7nDC`).** Daha sıcak ve husky; kıyı/denizci hissi güçlü.
3. **Aksan isteniyorsa: Sirius design_nuri_1.** Akdeniz rengini kontrollü verebilecek tek yol bu.
   Seçilirse kaydedilir ve tutarlılık için tüm satırlar aynı tasarımla üretilir. Ersan ve Nikos
   aksan için katalogdaki alternatifler; ikisinde de ton/telaffuz riski var.
- Seçim yapımcı ve kullanıcının dinlemesiyle kesinleşecek.
- Seçimden sonra ilk ücretli test satırı S12 olmalı (~45 karakter): "All the light I ever gave
  away... came back." Duygusal doruk ve elipsli nefes bu satırda olduğu için en iyi sınama bu.

---

## 2. Satır listesi (üretildi)

Tüm dosyalar `audio/` altında, ayar: David / multilingual_v2 / speed 0.8 / stability 0.6.
"Sınır" = çekim süresi − 0,5 sn. "Konuşma sonu" = dosyadaki son sessizliğin başladığı an
(dosya sonunda ~0,4 sn doğal kuyruk var). `assemble.py` dosyayı çekimin başına koyar.

| Çekim | Çekim süresi | Metin | Dosya | Dosya süresi | Konuşma sonu | Sınır | Sığıyor mu | task_id |
|---|---|---|---|---|---|---|---|---|
| S01 | 8 sn | Forty-one years. The same light. The same sea. | audio/vo_S01.mp3 | 7,11 sn | 6,71 sn | 7,5 | Evet (pay 0,4 sn, dar) | `b5a9d26b-a19a-49c4-80ef-69c18c72fe54` |
| S02 | 8 sn | Tomorrow, a machine keeps the watch. | audio/vo_S02.mp3 | 3,71 sn | 3,36 sn | 7,5 | Evet | `a981c69e-fa32-40aa-8f2f-7f4d9e0e1bce` |
| S03 | 7 sn | The light can turn itself now, they said. | audio/vo_S03.mp3 | 3,71 sn | 3,34 sn | 6,5 | Evet | `196a3caf-ac22-4acc-9a87-8afae6773de1` |
| S04 | 7 sn | I never knew who my light reached. | audio/vo_S04.mp3 | 3,37 sn | 2,89 sn | 6,5 | Evet | `a488d05e-9b24-40f4-9921-19b85b73cb99` |
| S06 | 6 sn | No ship ever sailed out there. Nothing ever did. | audio/vo_S06.mp3 | 5,09 sn | 4,70 sn | 5,5 | Evet (pay 0,4 sn) | `bfb2f6ff-ce49-4184-90ac-e69d6bff9ae3` |
| S07 | 8 sn | That was my signal. Two short... one long. | audio/vo_S07.mp3 | 5,43 sn | 5,05 sn | 7,5 | Evet | `8ddf3481-5f30-47bf-b2a0-5828ffb43301` |
| S09 | 8 sn | Forty-one years looking down. Tonight, I go down. | audio/vo_S09.mp3 | 7,18 sn | 6,78 sn | 7,5 | Evet (pay 0,3 sn, dar) | `c366f7d5-46e0-4122-89de-864483111533` |
| S12 | 7 sn | All the light I ever gave away... came back. | audio/vo_S12.mp3 | 5,25 sn | 4,80 sn | 6,5 | Evet | `729bee3d-d156-4583-b615-d0be7d650293` |
| S14 | 6 sn | To take me home. | audio/vo_S14.mp3 | 1,67 sn | 1,22 sn | 5,5 | Evet | `ec3f0811-f3f5-48b9-aa27-e9f2e3b6fb35` |
| S16 | 8 sn | Let the sea keep its own light now. | audio/vo_S16.mp3 | 3,66 sn | 3,28 sn | 7,5 | Evet | `560847bc-427a-49b5-9ca3-358bd3f70c32` |

Yeniden indirme: sonuç URL'si her zaman `https://files.genaipro.io/<task_id>.mp3` biçiminde
(ör. `https://files.genaipro.io/b5a9d26b-a19a-49c4-80ef-69c18c72fe54.mp3`). Görev bilgisi
`GET /v1/labs/task/<task_id>` ile de alınabilir. TTS görevleri `genaipro_tasks.jsonl`'a yazılmıyor.

### Ek (ücreti ödenmiş) alternatif çekimler, `audio/takes/`
| Dosya | Süre | task_id | Not |
|---|---|---|---|
| S09_alt_12266899.mp3 | 6,58 sn | `12266899-2951-408d-935a-e55a44825f03` | S09 ilk görevi ~25 dk takıldı, yeniden gönderildi; sonra o da tamamlandı. Daha kısa (pay 0,9 sn); S09 sıkışırsa bu kullanılabilir |
| S16_alt_1b8c67bc.mp3 | 3,19 sn | `1b8c67bc-fff8-4705-8cb0-556e448ec7cb` | Aynı durum, S16 |
| S12_mlv2_sp090_st050.mp3 | 4,44 sn | `e28bf0cc-7c66-4ff5-b902-0e7448a197b5` | Ayar sınaması |
| S12_v3_sp085_st050.mp3 | 4,44 sn | `e49a5a36-b93e-496a-b80c-04cd5dfe4206` | Ayar sınaması |

### Kredi dökümü (Voice AI, karakter)
- S12 sınaması: 3 × 44 = 132
- Kalan 9 satırın ilk turu: 347 (S09 ve S16 dahil; bu ikisi sunucuda takıldı ama ücretlendi)
- S09 + S16 yeniden gönderimi: 49 + 35 = 84
- **Toplam: 563** (bütçe ~1500). Bakiye 995.180.

### Sorunlar ve öneriler
- **Hiçbir satır sınırı aşmıyor.** Metin değiştirilmedi, hızlandırma gerekmedi.
- **S01 ve S09 dar (0,3–0,4 sn pay).** Konuşma çekimin 6,7–6,8. saniyesinde bitiyor; sonraki
  çekime geçişte cümle sonu kesilmesin diye kurguda V.O.'yu 0,0 sn'den başlatın, çekim sonuna
  çapraz geçiş koymayın. Gerekirse S09 için `takes/S09_alt_12266899.mp3` (6,58 sn) kullanılabilir,
  ya da ffmpeg `atempo=1.05` (tını bozulmadan ~0,35 sn kazanç). Yeniden üretime gerek yok.
- **S06 (6 sn):** 5,09 sn, sığıyor; taslaktaki risk gerçekleşmedi.
- **Düzey farkı:** satırlar arası ortalama düzey −18,1 ile −23,5 dB arasında (S07, S12 daha alçak/
  fısıltılı). Kurguda V.O.'ya ortak loudness normalizasyonu (ör. `loudnorm` I=−18 LUFS) uygulanmalı.
- **Servis notu:** toplu paralel gönderimde HTTP 429 (dakika limiti) ve 502 alındı; 2 görev ~25 dk
  "processing"te kaldı. Sonraki TTS işleri tek tek ve aralıklı gönderilmeli.

---

## 3. Müzik brief'i (taslak) → `audio/music.mp3`

- **Tür:** Minimal neoklasik / ambient. Sinematik ama seyrek.
- **Süre:** ~2:00 (118 sn görüntü + ~2 sn siyah/başlık). Sonda doğal kuyruk (decay) olmalı.
- **Tempo:** ~60 BPM; serbest ve rubato hissi. Ana motif fenerin dönüşüne bağlı yavaş bir nabız.
- **Enstrümanlar:** Felt (keçeli) piyano, sul tasto yaylı pad (viyola/çello), uzun drone.
  Çok hafif bowed vibrafon ya da kristal kâse ile ışık parıltısı. S07'den itibaren piyano veya
  çanla "kısa-kısa-uzun" ritmik motif (fenerin sinyali). Davul yok, vokal yok.
- **Duygu eğrisi:**
  - 0:00–0:30 (S01–S03): soğuk, yalnız. Tek piyano notaları ve drone. Çok alçak.
  - 0:30–0:58 (S04–S07): merak ve gerginlik. Pad açılır, "2 kısa 1 uzun" motifi doğar.
  - 0:58–1:20 (S08–S11): iniş. Ritim sabitlenir, yaylılar yavaşça büyür.
  - 1:20–1:42 (S12–S14): sıcak doruk. Majöre dönüş, en dolu an (yine de V.O.'nun altında kalır).
  - 1:42–2:00 (S15–S16): elektrikli uğultu geçişi. Müzik inceltilir, tek sıcak piyano motifiyle kapanır.
- **Referans tını:** Jóhann Jóhannsson, Ólafur Arnalds, Max Richter ("On the Nature of Daylight" inceliği).
- **Kaynak:** telifsiz kütüphane (ör. Uppbeat, Pixabay Music, YouTube Audio Library) ya da kullanıcının
  kendi parçası. genaipro'da müzik üretimi yok.

---

## 4. Miks notları (ön taslak, çekim listesi gelince kesinleşir)
- Diyalog yok, `DIALOGUE_IN_CLIP` yok, dudak senkronu riski yok.
- V.O.'lu çekimlerde V.O. baskın; klip sesi (rüzgâr/dalga) ~0.4, müzik −18…−20 dB altta.
- V.O.'suz çekimlerde (S05, S08, S10, S11, S13, S15) klip ortam sesi baskın (~0.8–1.0). S10'da dalgalar yükselir.
  S15'te saat mekanizması gıcırtısı kesilip elektrik uğultusu başlar; Veo üretmezse ses efekti gerekir.
- V.O. işleme: yakın mikrofon hissi, hafif sıcak EQ, oda yankısı neredeyse yok. İç ses olduğu için kuru kalmalı.
