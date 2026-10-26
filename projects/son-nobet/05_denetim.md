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
