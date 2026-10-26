# 04 — Ses Planı (TASLAK, tur 1: aday araştırması)

**Proje:** son-nobet ("The Last Watch") · **Dil:** İngilizce V.O. · **Tek ses:** NURİ (V.O.)
**Durum:** Aday araştırması BLOKE: ortamda `GENAIPRO_API_KEY` yok (`.env` de yok). Katalog sorgusu
ve Sirius önizlemeleri çalıştırılamadı. Anahtar tanımlanınca aşağıdaki komutlar aynen çalıştırılacak.
**Harcanan Voice AI kredisi:** 0

---

## 1. Ses tablosu

### Hedef ses profili (01_senaryo.md'den)
NURİ, 72 yaşında, Kuzey Egeli eski fener bekçisi. Ses alçak, hafif kısık, yavaş ve sakin olmalı.
Cümleler arasında nefes payı bırakır. Yaşlı ama çökmüş değil; kulağa yakın, fısıltıya yakın bir
yakınlığı var. Belirsiz bir Akdeniz aksanı olabilir ama şart değil.
Kaçınılacaklar: "trailer" bası, teatral/Shakespeare tınısı, belirgin İngiliz ya da Amerikan
radyo sunucusu sesi, titrek/hasta yaşlı sesi.

### A) ElevenLabs (Labs) katalog adayları: HENÜZ SORGULANMADI
Çalıştırılacak sorgular (ücretsiz):
```bash
python3 scripts/genaipro.py voices --gender male --age old --use-case narration --language en --limit 30
python3 scripts/genaipro.py voices --gender male --age old --language en --limit 30
for s in old narrator grandfather fisherman deep raspy husky gravelly whisper greek mediterranean; do
  python3 scripts/genaipro.py voices --search "$s" --gender male --limit 15
done
```
Seçim ölçütleri: age=old, sıcak ve alçak tını, yavaş tempo, "calm/soft/raspy/storyteller"
etiketleri. Ayrıca önizlemede soluk sesi ve sibilans yumuşaklığına bakılacak.

| # | Ad | voice_id | Özellikler | preview_url | Not |
|---|---|---|---|---|---|
| 1 | — | — | — | — | sorgu bekliyor |
| 2 | — | — | — | — | |
| 3 | — | — | — | — | |
| 4 | — | — | — | — | |

Model: `eleven_multilingual_v2` (sakin ve tutarlı anlatım için). Daha fazla nefes ve fısıltı
nüansı gerekirse `eleven_v3` ile karşılaştırılacak.

### B) Sirius ses tasarımı önizlemeleri: HENÜZ ÜRETİLMEDİ (ücretsiz, en fazla 2 istek)
```bash
python3 scripts/genaipro.py voice-design --out projects/son-nobet/audio/design_nuri_1.mp3 --instructions \
"A 72-year-old man, a retired lighthouse keeper from the North Aegean. Low, slightly husky, warm voice. Speaks slowly and calmly, with soft breaths between phrases, intimate and close to the microphone, almost a whisper. Old but not frail. Very light, unplaceable Mediterranean accent in English. Gentle, melancholic, never theatrical."

python3 scripts/genaipro.py voice-design --out projects/son-nobet/audio/design_nuri_2.mp3 --instructions \
"Elderly man in his seventies, deep and gravelly but soft, weathered by sea wind. Calm, unhurried storytelling in neutral English with only a faint Greek-Turkish coastal colouring. Quiet, close-mic intimacy, like confiding a secret at night. Steady, warm, tired but tender; no tremble, no drama."
```
| # | preview_id | Dosya | Tarif özeti | Not |
|---|---|---|---|---|
| 1 | — | audio/design_nuri_1.mp3 | kısık, fısıltıya yakın, hafif Akdeniz aksanı | bekliyor |
| 2 | — | audio/design_nuri_2.mp3 | daha derin/çakıllı, nötr İngilizce | bekliyor |

Kayıt (`voice-design-save`) yalnızca yapımcı onayından sonra yapılacak (hesap başına en fazla 3 tasarım).

### Ön öneri (dinleme öncesi)
- **Birincil yol: Labs katalog sesi.** İngilizce V.O.'da en olgun ve tutarlı yol bu. 10 satırın
  hepsinde aynı tını korunur ve voice_id ile birebir tekrar üretilebilir.
- **Sirius tasarımı:** Katalogda "aksan + yaşlı + fısıltı yakınlığı" üçünü birden taşıyan ses
  çıkmazsa yedek olarak kullanılır. Hafif Akdeniz aksanı ancak tasarımla kontrollü elde edilebilir.
- Nihai seçim yapımcı ve kullanıcının önizlemeleri dinlemesiyle yapılacak.
- Test cümlesi (ücretli TTS, onaydan sonra): "All the light I ever gave away... came back."
  Duygusal doruk satırı ve elipsli nefes bu satırda olduğu için en iyi sınama bu.

---

## 2. Satır listesi (senaryodan; dosyalar henüz üretilmedi)

| Çekim | Süre | Metin | Dosya |
|---|---|---|---|
| S1 | 8 sn | Forty-one years. The same light. The same sea. | audio/vo_S1.mp3 |
| S2 | 8 sn | Tomorrow, a machine keeps the watch. | audio/vo_S2.mp3 |
| S3 | 7 sn | The light can turn itself now, they said. | audio/vo_S3.mp3 |
| S4 | 7 sn | I never knew who my light reached. | audio/vo_S4.mp3 |
| S6 | 6 sn | No ship ever sailed out there. Nothing ever did. | audio/vo_S6.mp3 |
| S7 | 8 sn | That was my signal. Two short... one long. | audio/vo_S7.mp3 |
| S9 | 8 sn | Forty-one years looking down. Tonight, I go down. | audio/vo_S9.mp3 |
| S12 | 7 sn | All the light I ever gave away... came back. | audio/vo_S12.mp3 |
| S14 | 6 sn | To take me home. | audio/vo_S14.mp3 |
| S16 | 8 sn | Let the sea keep its own light now. | audio/vo_S16.mp3 |

Toplam yaklaşık 370 karakter, yani tek tur üretim ~370 Voice AI kredisi. 2 tur denemeyle ~750.
Çekim ID'leri yönetmenin `03_cekim_listesi.json`'ındaki ID biçimine göre (S01 ya da S1) kesinleşecek.
Süre riski: S6 (6 sn, 9 kelime, yavaş tempo) sınırda. Gerekirse `--speed 1.05–1.1` ya da çekimi 7 sn yapmak önerilecek.

---

## 3. Müzik brief'i (taslak) → `audio/music.mp3`

- **Tür:** Minimal neoklasik / ambient. Sinematik ama seyrek.
- **Süre:** ~2:00 (118 sn görüntü + ~2 sn siyah/başlık). Sonda doğal kuyruk (decay) olmalı.
- **Tempo:** ~60 BPM; serbest ve rubato hissi. Ana motif fenerin dönüşüne bağlı yavaş bir nabız.
- **Enstrümanlar:** Felt (keçeli) piyano, sul tasto yaylı pad (viyola/çello), uzun drone.
  Çok hafif bowed vibrafon ya da kristal kâse ile ışık parıltısı. S7'den itibaren piyano veya
  çanla "kısa-kısa-uzun" ritmik motif (fenerin sinyali). Davul yok, vokal yok.
- **Duygu eğrisi:**
  - 0:00–0:30 (S1–S3): soğuk, yalnız. Tek piyano notaları ve drone. Çok alçak.
  - 0:30–0:58 (S4–S7): merak ve gerginlik. Pad açılır, "2 kısa 1 uzun" motifi doğar.
  - 0:58–1:20 (S8–S11): iniş. Ritim sabitlenir, yaylılar yavaşça büyür.
  - 1:20–1:42 (S12–S14): sıcak doruk. Majöre dönüş, en dolu an (yine de V.O.'nun altında kalır).
  - 1:42–2:00 (S15–S16): elektrikli uğultu geçişi. Müzik inceltilir, tek sıcak piyano motifiyle kapanır.
- **Referans tını:** Jóhann Jóhannsson, Ólafur Arnalds, Max Richter ("On the Nature of Daylight" inceliği).
- **Kaynak:** telifsiz kütüphane (ör. Uppbeat, Pixabay Music, YouTube Audio Library) ya da kullanıcının
  kendi parçası. genaipro'da müzik üretimi yok.

---

## 4. Miks notları (ön taslak, çekim listesi gelince kesinleşir)
- Diyalog yok, `DIALOGUE_IN_CLIP` yok, dudak senkronu riski yok.
- V.O.'lu çekimlerde V.O. baskın; klip sesi (rüzgâr/dalga) ~0.4, müzik −18…−20 dB altta.
- V.O.'suz çekimlerde (S5, S8, S10, S11, S13, S15) klip ortam sesi baskın (~0.8–1.0). S10'da dalgalar yükselir.
  S15'te saat mekanizması gıcırtısı kesilip elektrik uğultusu başlar; Veo üretmezse ses efekti gerekir.
- V.O. işleme: yakın mikrofon hissi, hafif sıcak EQ, oda yankısı neredeyse yok. İç ses olduğu için kuru kalmalı.
