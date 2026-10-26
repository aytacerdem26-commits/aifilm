# The Last Watch — Süreklilik ve Kalite Denetimi

## Anahtar kare denetimi (2026-10-26)

Kaynaklar: `02_stil_rehberi.md`, `01_senaryo.md`, `03_cekim_listesi.json`, `refs/*.png`.
32 başlangıç varyantı + 4 bitiş varyantı Read ile tek tek incelendi.
Kontakt tabaka: `qa/kontakt_keyframes.jpg` (seçilen kareler; S13/S15 başlangıç + bitiş yan yana).

### Özet

- **ONAY (11):** S01, S02, S03, S04, S06, S07, S08, S09, S14, S15 (+end), S16
- **YENİDEN ÜRET (5 istek ≈ 5 kredi):** S05, S10, S11, S12, S13 (yalnızca başlangıç karesi, düzenleme olarak)
- JSON: `keyframe_file` / `end_keyframe_file` / `keyframe_url` seçilen varyanta çekildi; ONAY'lar
  `keyframe_approved`, diğerleri `keyframe_done` + `notes`'ta gerekçe.

### En kritik 3 sorun

1. **Denizdeki ışık ay gibi büyük ve ufukta (S05, S11, S12, S13).** Küre ya ufuk çizgisine oturmuş
   turuncu bir disk (ay doğuşu gibi okunuyor, gökte gerçek ay da var), ya da S12'de kafanın ~2 katı
   bir balon. S07'deki minik nokta ile tutarsız. Muhtemel kaynak: `cape_night.png` referansındaki
   kürenin baskınlığı. Prompt'larda kürenin ufkun **altında**, yakın suyun üstünde ve "aydan çok küçük"
   olduğu açıkça yazılmalı; gökteki ay disk olarak görünmemeli.
2. **Tek karakter kuralı ihlali / kolaj figür (S10, S11).** S10 v2 ve S11 v1'de iki Nuri var; S10 v1'de Nuri
   kameraya poz veren, kuleyle neredeyse aynı boyda yapıştırılmış bir figür. Aksiyon (kapıdan çıkıp kayalarda
   ilerleme) yok.
3. **S12 duygu karesi tutmuyor.** Senaryonun anahtar anı ("yüz ilk kez alttan sıcak altın") iki varyantta da
   yok: yüz soğuk/düz, Nuri tam boy kameraya bakıyor.

### Özel kontroller

- **✦ Filigran (sağ alt, ~x1278 y670):** Seçilen karelerden S01, S03, S07, S13 (+S13_end) filigranlı;
  iki varyantta da vardı, tek başına red sebebi sayılmadı. Filigransız varyant olan yerlerde o seçildi
  (S02, S04, S06, S08, S09, S12-yedek, S14, S15, S16). **Kurgucu:** bu kliplerde
  `delogo=x=1250:y=645:w=56:h=52` (1376x768 ölçeğinde; 1080p'de ×1.395) ya da hafif kırpma uygulamalı.
  **Öneri (kredisiz):** yeniden üretimden önce `cape_night.png` / `stairwell.png` / `cape_dawn.png`'nin
  filigransız kopyası (`ffmpeg delogo`) referans olarak verilirse sızıntı azalır.
- **Küçük dosyalar (S01, S03, S07, S13):** Fazla karanlık değil; büyük, düz gece gökyüzü/deniz alanları
  nedeniyle iyi sıkışıyorlar. Gölgelerde mavi detay korunmuş, siyahlar ezilmemiş. Sorun yok.
- **S13 fener yüksekliği:** Uzatılmış kolla göğüs-omuz hizasında; senaryodaki "göğüs hizası"na yeterince yakın.
  Kol gövdeye yakın değil ama el kadrajda küçük. Kabul.
- **Nuri tutarlılığı:** Bere, krem balıkçı kazağı, açık lacivert palto + pirinç düğmeler, kısa beyaz sakal bütün
  seçilen karelerde var. S06 v2'nin yüzü referanstan biraz daha sert/kırışık ama aynı kişi olarak okunuyor.
- **Yön (180°):** S04 v2, S06 v2, S07 v1 seçimleriyle galeri sahnesinde lamba odası solda, Nuri sağa (denize)
  bakıyor. S13 ve S14'te de sağa bakıyor. Yeni S05 bu yönle çelişmemeli (bkz. prompt).

### Çekim başına karar

| ID | Seçilen | Karar | Gerekçe |
|---|---|---|---|
| S01 | v1 | ONAY | Huzme belirgin, kule ay altında, köpüklü kayalar. Filigran (iki varyantta da). |
| S02 | v2 | ONAY | Silme hareketi, eller doğal, dolap + yeşil LED kadrajda (S03'e köprü). Filigransız. |
| S03 | v1 | ONAY | Ön planda dolap, arkada flu Nuri ona bakıyor; kancada fener görünür (S08 sürekliliği). Dolapta yazı yok. Filigran. |
| S04 | v2 | ONAY | Korkuluğa yaslanmış, huzme başının üstünde, fırtınalı deniz. v1 alacakaranlık gibi aydınlıktı. |
| S05 | v2 (yedek) | YENİDEN ÜRET | Küre ufukta ay boyunda disk ("ikinci ay"); v1'de lamba odası aynalanmış (artefakt); "kule görünmesin" uygulanmamış. |
| S06 | v2 | ONAY | Gözlerde minik altın yansıma (senaryodaki an), sağa bakış S04 ile tutarlı. |
| S07 | v1 | ONAY | Küre küçük net nokta; geografi S04 v2 ile aynı. v2'de yön ters. Filigran. |
| S08 | v1 | ONAY | Kancadaki fenere uzanıyor; dolap + LED arkada. |
| S09 | v2 | ONAY | Tam tepe kabuk spirali, yarık pencere, sönük fener. v1'de siyah pillarbox bantları. |
| S10 | v1 (yedek) | YENİDEN ÜRET | v2: iki Nuri. v1: poz veren, kuleyle aynı boyda kolaj figür; aksiyon yok. |
| S11 | v2 (yedek) | YENİDEN ÜRET | v1: iki Nuri. v2: küre ufukta ay boyunda (ay doğuşu gibi), "20 m açıkta" değil. |
| S12 | v2 (yedek) | YENİDEN ÜRET | Yüz alttan sıcak aydınlanmıyor, kameraya poz, küre kafanın ~2 katı. v1'de filigran. |
| S13 | v1 + end_v2 | YENİDEN ÜRET (yalnız başlangıç) | Küre ufukta ay boyunda; S12'deki konumla ve "fenerin 1 m önünde" tarifiyle çelişiyor. end_v2 = v1 ile aynı poz (SSIM 0.95), korunur. |
| S14 | v1 | ONAY | Alttan sıcak ışık, nemli gözler, sağa bakış. |
| S15 | v1 + end_v2 | ONAY | Başlangıçta sıcak turuncu, bitişte soğuk beyaz; aynı kadraj (SSIM 0.96). Kubbe yeşilimsi gri, şafakta önemsiz. |
| S16 | v2 | ONAY | Sırtı dönük uzaklaşıyor, tek sıcak nokta fener, soğuk beyaz huzme, pembe ufuk. v1 kameraya doğru yürüyordu. |

### Yeniden üretim önerileri (İngilizce; CHAR_/LOC_/PROP_/LIGHT_/STYLE bloklar kelimesi kelimesine korunur, yalnızca kadraj cümlesi ve ekler değişir)

**Uyarı (yapımcıya):** `genaipro.py keyframes --ids …` çıktıyı `keyframes/<ID>_v1/_v2.png` üzerine yazar.
Yedekler kaybolmasın diye önce kopyala: `cp keyframes/S13_v1.png keyframes/S13_base.png` (S13 referansı bu
kopya olmalı); S05/S10/S11/S12 yedekleri için de `_old` kopyası önerilir.

**S05**: refs: yalnızca `refs/lamp_room.png` (cape_night çıkarılsın; büyük küreyi öğretiyor). Kadraj cümlesini değiştir:
> Point-of-view wide shot from the lighthouse gallery looking straight out to the open sea; only the top rail of the black iron railing, dark and soft, runs across the bottom edge of frame; no lantern room, no glass panes, no lighthouse structure in frame; a low dark horizon over an empty navy-black sea; the moon hidden behind thick cloud, no moon disc visible anywhere; dead centre exactly on the horizon: far away on the horizon, tiny: [PROP_SEA_LIGHT]; at this distance it is only a tiny pinprick of warm golden light, many times smaller than the moon would be, with a thin faint golden glint on the water beneath it; exactly one light source at sea; no people, no boats.

**S10**: refs: `refs/nuri.png`, `refs/cape_night.png`.
> Wide low-angle shot from the wet rocks near the waterline; the tall white lighthouse fills the left half of frame and rises into the night sky with its warm beam turning; Nuri small in frame, about one fifth of the frame height, a few steps out from the small arched wooden door at the base of the tower, seen in three-quarter view from behind as he carefully picks his way down across the wet seaweed-covered rocks toward the sea, head bowed watching his footing, not looking at the camera, the unlit lantern hanging from one hand at his side: [PROP_LANTERN unlit]; exactly one person in the image, a single figure only; no glowing sphere in frame. [CHAR_NURI] …

**S11**: refs: `refs/nuri.png`, `refs/cape_night.png`.
> Shot from behind Nuri, full figure, exactly one person in the image, standing at the very edge of the wet rocks facing the open sea, the unlit lantern hanging at his side: [PROP_LANTERN unlit]; some twenty metres out over the water, well below the horizon line with dark sea visible behind and above it, approaching: [PROP_SEA_LIGHT]; the sphere no larger in frame than his head, far smaller than a moon; the moon hidden behind clouds, no moon disc visible; the crests of the waves between them catching gold. …

**S12**: refs: `refs/nuri.png`, `refs/cape_night.png`.
> Medium shot, waist up, Nuri facing camera on the rocks but looking down at the light below him, not looking into the lens, a quiet awed expression; at the bottom edge of frame, partly cut off by the frame edge and no bigger than his head, just above the waves at the foot of the rocks: [PROP_SEA_LIGHT]; strong steady warm golden light from below on his chin, cheeks, beard and the cream sweater, the only warm face in the cold blue night, everything else steel-blue; the dark tower soft and out of focus in the background, shallow depth of field; exactly one person; the unlit lantern hanging at his side: [PROP_LANTERN unlit]. …

**S13 (başlangıç, düzenleme)**: refs: `keyframes/S13_base.png` (= mevcut S13_v1), `refs/nuri.png`. `end_keyframe_file` = `S13_end_v2.png` kalır.
> Keep the first reference image exactly: same framing, same man, same pose with the raised unlit lantern at chest height, same tower, rocks, sky and sea. Change only the glowing light: remove the large glowing disc from the horizon entirely and place it close instead, about one metre in front of and slightly below the lantern, hovering just above the water at the foot of the rocks: [PROP_SEA_LIGHT]; the sphere about the size of the lantern, much smaller than a moon; it casts warm gold light on his face, hand and coat; no glowing disc on the horizon. [LIGHT_NIGHT], [STYLE_SUFFIX], no text, no watermark, no logo

Not: S13 düzenlemesi başarısız olursa (kompozisyon kayarsa), yeni başlangıç karesinden bitiş karesi de
yeniden üretilmeli (+1 kredi).

---

## Anahtar kare denetimi — 2. tur (2026-10-26)

Kapsam: yalnız S05, S10, S11, S12, S13 (yeniden üretim/düzenleme). 10 yeni varyant Read ile incelendi,
eski sürümler (`keyframes/old/`) karşılaştırma için tutuldu. Kontakt tabaka (16 çekim, S13/S15
başlangıç + bitiş = 18 kare): `qa/kontakt_keyframes_v2.jpg`.

### Özet

- **ONAY (5):** S05 (v2), S10 (v2), S11 (v2*), S12 (v2*), S13 (edit_v1 + end_v2) → 16/16 `keyframe_approved`.
- **\* Klipten önce kredisiz düzeltme şart (S11, S12):** huzme rengi (aşağıda). Yeniden üretim gerekmiyor, 0 kredi.
- JSON: `keyframe_file` / `keyframe_url` seçilen varyanta çekildi, `notes`'a 2. tur gerekçesi eklendi; JSON geçerli,
  tüm dosya yolları mevcut, toplam süre 118 sn.

### En kritik 3 sorun

1. **S11/S12 fener huzmesi soğuk beyaz-mavi (hue ~205°)** — S10 ve S13'te amber (hue ~28°). Huzme kadrajın yalnız
   ~%1–1.5'i (S10'daki amber huzme ~%11) ve doygunluğu düşük, ama S10→S11 ve S12→S13 kesmelerinde amber→beyaz→amber
   sıçraması kontakt tabakada açıkça görünüyor; ayrıca filmin S15'teki "sıcak ışık → soğuk elektrik" dönüşümünü
   erken ele veriyor. Klipte huzme döndüğü için daha da dikkat çekecek. **İzleyicinin fark edeceği bir hata.**
   Çözüm kredisiz: `scripts/warm_beam.py` ile yalnız huzme kutusu amber'e çekilir (test önizlemesi:
   `qa/S11_S12_huzme_amber_onizleme.png`, temiz sonuç):
   - `python3 -I scripts/warm_beam.py projects/son-nobet/keyframes/S11_v2.png projects/son-nobet/keyframes/S11_v2_warm.png 180 30 820 170`
   - `python3 -I scripts/warm_beam.py projects/son-nobet/keyframes/S12_v2.png projects/son-nobet/keyframes/S12_v2_warm.png 740 40 636 120`
   - Sonra `keyframe_file` → `*_v2_warm.png` (görüntü üretici/yapımcı). `video_prompt`'lara ek:
     S11 *"the lighthouse beam behind him glows warm amber (#F2A541) as it turns, never white"*,
     S12 *"the distant lighthouse beam glows warm amber (#F2A541), never white"*.
   - Kök neden: S11/S12 `image_prompt`'unda yalnız "the lighthouse beam sweeping across the water" yazıyor, "warm" yok,
     ve cape_night referansı çıkarıldı. İleride bu iki çekim yeniden üretilirse: *"the lighthouse beam is warm amber
     (#F2A541), no white light anywhere"*.
2. **S10 ve S11 benzer arkadan kadraj** (kule solda, Nuri arkadan). S11'de Nuri ~1.4x büyük ve küre giriyor, atlama
   kesmesi gibi durmuyor; kurgucu S10'u Nuri hareket hâlindeyken kesmeli. Red sebebi değil.
3. **Filigran:** S05 v2 ve S11 v2'de ✦ var (iki varyantta da); S13 start filigransız ama end_v2 filigranlı.
   Kurgucu bu üç klipte 1. turdaki `delogo` ayarını uygulamalı.

### Küre sürekliliği S11 → S12 → S13

| Çekim | Konum | Ölçek | Yorum |
|---|---|---|---|
| S11 v2 | Ufkun altında, ~20 m açıkta, kadraj sağı | Nuri'nin kafasından küçük (~35 px / kafa ~60 px) | Uzaktan yaklaşan kafa boyu küre — doğru |
| S12 v2 | Kayaların dibinde, dalgaların üstü, kadraj sol altı | Kafadan biraz büyük (~140 / ~120 px) | Kameraya yakın; ters açıda Nuri'nin sağında → S11 ile tutarlı |
| S13 edit_v1 | ~2 m açıkta suyun üstü, fenerin önü-altı | Kafa/fener boyu (~80 px) | S12 ile aynı mesafe hissi; ufukta disk yok |

Üçünde de küre suyun hemen üstünde, altın yansımalı; ay boyu disk sorunu giderildi. Geografi (kule solda, deniz sağda;
S12 ters açıda kule sağda) S10–S13 boyunca tutarlı.

### Çekim başına karar

| ID | Seçilen | Karar | Gerekçe |
|---|---|---|---|
| S05 | v2 | ONAY | Ufukta küçük sıcak nokta + suda altın iz; ay diski, kule, cam yok; korkuluk temiz. v1'de korkuluk hizasında anlamsız köpük bandı. ✦ filigran. |
| S10 | v2 | ONAY | Tek Nuri, arkadan başı eğik kayalarda denize iniyor; kemerli kapı, amber huzme. ~%55–60 yükseklik ama kuleden önde olduğu için perspektif doğal. v1: Nuri kuleden büyük, ölçek bozuk. |
| S11 | v2 | ONAY (+kredisiz huzme düzeltmesi) | Tek kişi, küre ufkun altında, kafa boyundan küçük, dalga tepeleri altın. Huzme soğuk beyaz → warm_beam. v1: kule sağda (geografi ters), küre ufukta ay gibi. ✦ filigran. |
| S12 | v2 | ONAY (+kredisiz huzme düzeltmesi) | Önden bel üstü, aşağı bakıyor; sakal altı, yanak ve yaka sıcak altın — alttan ışık okunuyor (kısmi ama yeterli; video_prompt titreşimi güçlendiriyor). Palto açık, filigran yok. Huzme soğuk beyaz → warm_beam. v1: yana dönük, yüz önden aydınlık. |
| S13 | edit_v1 + end_v2 | ONAY | Kadraj/poz end_v2 ile birebir; küre fener boyunda, kayaların dibinde; huzme amber. edit_v2'de küre fenerin ~2 katı. |

### Yapımcıya

- Onaylanan: S01–S16 (16/16). Reddedilen: yok. Ek kredi: 0.
- Klip üretiminden önce S11/S12 için iki `warm_beam.py` komutu + `keyframe_file` değişikliği + iki `video_prompt` eki yapılmalı.
