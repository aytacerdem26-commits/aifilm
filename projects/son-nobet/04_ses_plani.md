# 04 — Ses Planı (TASLAK: ses adayları hazır, seçim bekliyor)

**Proje:** son-nobet ("The Last Watch") · **Dil:** İngilizce V.O. · **Tek ses:** NURİ (V.O.)
**Durum:** Aday araştırması tamamlandı (tur 1). Dinleme ve seçim yapımcı/kullanıcıda.
Henüz TTS üretilmedi, tasarım kaydedilmedi.
**Harcanan Voice AI kredisi:** 0 (katalog ve Sirius önizlemesi ücretsiz). Kalan aktif bakiye
yaklaşık 995.743 karakter, bitiş tarihi 2026-11-18.

---

## 1. Ses tablosu

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

## 2. Satır listesi (senaryodan; dosyalar henüz üretilmedi)

| Çekim | Süre | Metin | Dosya |
|---|---|---|---|
| S01 | 8 sn | Forty-one years. The same light. The same sea. | audio/vo_S01.mp3 |
| S02 | 8 sn | Tomorrow, a machine keeps the watch. | audio/vo_S02.mp3 |
| S03 | 7 sn | The light can turn itself now, they said. | audio/vo_S03.mp3 |
| S04 | 7 sn | I never knew who my light reached. | audio/vo_S04.mp3 |
| S06 | 6 sn | No ship ever sailed out there. Nothing ever did. | audio/vo_S06.mp3 |
| S07 | 8 sn | That was my signal. Two short... one long. | audio/vo_S07.mp3 |
| S09 | 8 sn | Forty-one years looking down. Tonight, I go down. | audio/vo_S09.mp3 |
| S12 | 7 sn | All the light I ever gave away... came back. | audio/vo_S12.mp3 |
| S14 | 6 sn | To take me home. | audio/vo_S14.mp3 |
| S16 | 8 sn | Let the sea keep its own light now. | audio/vo_S16.mp3 |

Toplam yaklaşık 370 karakter, yani tek tur üretim ~370 Voice AI kredisi. 2 tur denemeyle ~750.
Dosya adları çekim listesindeki ID biçimini izler (`vo_S01.mp3` … `vo_S16.mp3`); V.O.'suz çekimler için dosya yok.
Süre riski: S06 (6 sn, 9 kelime, yavaş tempo) sınırda. Gerekirse `--speed 1.05–1.1` ya da çekimi 7 sn yapmak önerilecek.

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
