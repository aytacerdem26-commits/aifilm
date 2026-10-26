# The Last Watch (Son Nöbet) — Stil Rehberi

> Kaynak: `00_brief.md`, `01_senaryo.md` (rev. 2, onaylı). Bu dosyadaki İngilizce bloklar
> (`STYLE_SUFFIX`, `LIGHT_*`, `CHAR_*`, `LOC_*`, `PROP_*`) bütün görsel ve video prompt'larında
> **kelimesi kelimesine** kopyalanır; kısaltılmaz, yeniden yazılmaz, sıralaması değiştirilmez.

---

## 1. Görsel stil

- **Tür:** Sinematik gerçekçi; büyülü gerçekçilik ama "fantastik" görünüm yok. Denizdeki ışık
  dışında her şey dokunsal, ağır, gerçek.
- **Format:** 35mm film negatifi hissi, anamorfik lens (yatay oval bokeh, ince yatay lens
  flare'ler — yalnızca sıcak ışık kaynaklarında), ince ve organik film grain, hafif halation.
- **Doku:** Tuz lekeli cam, soyulmuş boya, ıslak taş, kalın yün. Yüzeyler mat, plastik/CGI
  parlaklığı yok.
- **Referans duygu:** Roger Deakins gece ışığı, *The Lighthouse* (2019) dokusu ama renkli;
  *Ida*/*Leviathan* sadeliği.

## 2. Renk paleti ve ışık

| Rol | Renk | Hex |
|---|---|---|
| Gece gölgesi / deniz | Lacivert-siyah | `#0B1626` |
| Ay ışığı / gece dolgu | Soğuk çelik mavi | `#3E5A7A` |
| Fener huzmesi / lamba / denizdeki ışık | Sıcak amber | `#F2A541` |
| Fener çekirdeği / alev merkezi | Bal sarısı | `#FFD27A` |
| Şafak gökyüzü | Soluk mavi-gri | `#A7B4C2` |
| Şafak ufuk çizgisi | İnce pembe | `#E8B4B8` |

Yardımcı: otomatik sistemin ışığı **soğuk beyaz** `#E6F0FF`; dolap LED'i **yeşil** `#39FF88`
(küçük nokta, asla ortamı aydınlatmaz).

**Işık yaklaşımı**
- **Gece (S1–S14):** Ortam düşük anahtarlı, soğuk mavi ay ışığı. Tek sıcak kaynak Fresnel
  merceği/huzmesi (S1–S11) ve sonra denizdeki ışık ve fener (S11–S16). Gece sahnelerinde
  sıcak ışık hep *uzaklaşır*; Nuri'nin yüzü S12'ye kadar asla doğrudan sıcak, önden ve uzun
  süre aydınlanmaz (huzme yalnızca geçer).
- **S12–S14:** İlk kez sıcak ışık alttan ve sabit — yüz altın, çevre mavi kalır.
- **Şafak (S15–S16):** Düz, yumuşak, gölgesiz soluk mavi-gri; ufukta ince pembe çizgi.
  Kuledeki yeni ışık soğuk beyaz. Kadrajdaki tek sıcak nokta Nuri'nin feneri.
- Siyahlar ezilmez; gölgelerde mavi detay kalır. Highlights amber'de yumuşak döner.

## 3. Kamera dili

- **Lens:** Anamorfik 2x hissi; genişlerde 32–40mm, ortalarda 50mm, yakınlarda 75–100mm.
  Kadraj 16:9 (anamorfik görünüm ama letterbox yok).
- **Derinlik:** Yakın ve ortalarda sığ alan derinliği (f/2–2.8), arka plan yumuşak.
  Genişlerde derin; kule ve ufuk okunur.
- **Hareket:** Yavaş ve sabırlı. Tripod/sabit kamera, çok yavaş push-in veya yavaş pan.
  El kamerası yok, hızlı hareket yok, drone hissi yok (S1 ve S16 hariç, yine de durağan).
  Huzme ve dalgalar hareket eder; kamera neredeyse durur.
- **Kompozisyon:** Geniş negatif alan, ufuk alçak, Nuri sıklıkla kadrajın üçte birinde.
  S9 tam tepe (top-down) kadraj.

## 4. Sabit İngilizce bloklar

### STYLE_SUFFIX (her prompt'un sonuna, tek satır)

```
cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9
```

### Işık blokları (STYLE_SUFFIX'ten hemen önce, sahneye göre biri)

`LIGHT_NIGHT` (S1–S14):
```
night, cold steel-blue moonlight and deep navy shadows, the only warm light is amber-gold (#F2A541), strong warm-cold contrast
```

`LIGHT_DAWN` (S15–S16):
```
early dawn, soft flat pale blue-grey light, overcast sky with a thin pale pink line on the horizon, no direct sun, quiet and cold
```

### CHAR_NURI

```
NURI, a 72-year-old man of North Aegean Mediterranean appearance, tall but slightly stooped, lean build; deeply lined weathered face with wind-reddened cheeks, short fully white-grey beard neatly trimmed close to the jaw, pale grey eyes, tired but warm expression; wearing a dark grey knitted wool beanie covering his hair, a thick cream cable-knit fisherman's sweater with a roll neck, a knee-length navy wool pea coat with two rows of brass buttons worn open, dark grey wool trousers, black knee-high rubber boots
```

Notlar: Bere hiçbir çekimde çıkarılmaz (saç görünmez). Palto **hep açık**. Gözlük, yüzük,
saat, atkı, eldiven yok. Fener sahnedeyse `PROP_LANTERN` ayrıca eklenir.

### PROP_LANTERN

Söndürülmüş hâli (S8–S13):
```
an old brass hurricane lantern with a clear glass chimney and a wire carrying handle, tarnished and worn brass, unlit
```
Yanan hâli (S13 sonu, S14, S16) — yukarıdaki satırın `unlit` kelimesi yerine:
```
lit from within by a small warm flickering flame, soft amber glow
```

### PROP_SEA_LIGHT (S5, S7, S11, S12, S13)

```
a single softly glowing warm golden sphere of light hovering just above the sea surface, about the size of a human head, no flame, no object inside, smooth round glowing core with a soft diffuse halo, colour #FFD27A fading to amber #F2A541, reflected as a golden shimmer on the water below
```

Notlar: Uzak çekimlerde (S5, S7) başına `far away on the horizon, tiny` eklenir; boyut
tarifi değişmez. Asla alev, yıldız, UFO, gemi feneri, ışın veya parçacık yağmuru değil.

### LOC_LAMP_ROOM (lamba odası + galeri)

```
the lantern room at the top of an old white stone lighthouse with a black-painted iron cupola: an octagonal room walled in tall salt-streaked glass panes with black iron frames; at the centre a large honey-coloured Fresnel lens of stacked concentric glass prisms with a warm yellow-orange light turning inside it; brass fittings and rails, an iron floor with peeling grey-green paint; in one corner a brand-new plain white metal electrical cabinet with no labels and no text, one small green LED indicator light; an iron wall hook beside the stairwell hatch; a glass door opening onto a narrow circular outer gallery with a black iron railing, black sea far below, wind
```

Galeri çekimleri (S4–S7) için başına `outside on the narrow gallery of` eklenebilir; blok değişmez.

### LOC_STAIRWELL

```
a narrow cast-iron spiral staircase winding down inside an old stone lighthouse tower, curved stone walls with flaking whitewash, one small vertical slit window letting in a shaft of cold blue moonlight across the iron steps, otherwise dark; seen from above the spiral narrows downward like the inside of a seashell
```

### LOC_CAPE (kayalık burun, kule dışı, kıyı patikası)

```
a rocky North Aegean headland: dark grey wet rocks covered in seaweed running from the foot of a tall white stone lighthouse with a black iron cupola down into the sea, waves breaking over the rocks in white foam; a small arched wooden door at the base of the tower; a narrow dirt coastal path lined with dry pale grass curving inland away from the tower; open sea to the horizon
```

Gece: `LIGHT_NIGHT` + `navy-black sea, moon between clouds, the lighthouse beam sweeping across the water`.
Şafak: `LIGHT_DAWN` + S15'ten sonra `the lighthouse now shows a cold white electric light`.

### Prompt montaj sırası

`[çekim/kadraj tarifi] + [CHAR_NURI] + [PROP_*] + [LOC_*] + [LIGHT_*] + STYLE_SUFFIX`

## 5. Kaçınılacaklar

- İkinci bir insan, siluet, kalabalık, gemi, tekne, kuş sürüsü (tek karakter kuralı).
- Ekranda her türlü yazı, logo, etiket, sayı, filigran — özellikle beyaz dolapta.
- Nuri'de kıyafet değişimi: kapalı palto, berenin olmaması, farklı renk kazak, ayakkabı,
  gözlük, uzun/dağınık sakal, kel ya da görünür saç.
- Denizdeki ışıkta alev, yıldız şekli, ışın huzmesi, kıvılcım, UFO/teknoloji görünümü,
  renk değişimi (mavi/beyaz olmamalı).
- Doymuş turuncu-turkuaz "teal & orange" klişesi, HDR, aşırı keskinlik, plastik cilt,
  CGI/oyun görünümü, çizgi film/illüstrasyon.
- Güneşli, berrak gökyüzü; şafakta güçlü güneş diski.
- Modern objeler (telefon, el feneri, LED lamba) — beyaz dolap ve yeşil LED dışında.
- Hızlı kamera, el kamerası sarsıntısı, Dutch angle.
- Ellerin kadrajın merkezinde ve detaylı olduğu kompozisyonlar (el anatomisi riski).

## 6. Referanslar

| Blok | Dosya | İçerdiği ek bloklar |
|---|---|---|
| `CHAR_NURI` + `PROP_LANTERN` | `refs/nuri.png` | fener elinde, sönük |
| `LOC_LAMP_ROOM` | `refs/lamp_room.png` | Fresnel, beyaz dolap + yeşil LED, kanca, galeri kapısı |
| `LOC_CAPE` (gece) + `PROP_SEA_LIGHT` | `refs/cape_night.png` | denizdeki ışık küre, kule, huzme |
| `LOC_STAIRWELL` | `refs/stairwell.png` | — |
| `LOC_CAPE` (şafak) — opsiyonel | `refs/cape_dawn.png` | soğuk beyaz yeni ışık, patika |

`PROP_LANTERN` → `refs/nuri.png`, `PROP_SEA_LIGHT` → `refs/cape_night.png` üzerinden referanslanır
(ayrı prop isteği yok).

---

## 7. Referans üretim planı

> **Bu turda çalıştırılmadı** — genaipro.io bu ortamdan erişilemiyor. Komutlar erişim
> sağlandığında `/home/user/aifilm` kökünden sırayla çalıştırılmak üzere hazırdır.
> Her istek 1 kredi (4 varyant dahil). Her adımdan sonra `_v1…_v4` Read ile incelenir,
> en iyisi `refs/<ad>.png` olarak kopyalanır; sonraki adım ancak bu dosya varken başlar.

**Toplam:** zorunlu 4 istek = **4 kredi**; opsiyonel şafak ile **5 kredi**.
Film üretimi ~32–33 kredi → toplam **37–38 / ~40**. Referans yeniden üretimi için pay ~2 kredi;
yeniden üretim gerekirse önce opsiyonel 5. istekten vazgeçilir.

### 1) refs/nuri.png — karakter sayfası + fener (1 kredi)

Seçim kriteri: yüz ve kıyafet bloğa birebir uyuyor, palto açık, pirinç düğmeler görünür,
fener sönük ve okunur, yazı/ikinci kişi yok.

```bash
python3 scripts/genaipro.py image --n 4 --aspect 16:9 \
  --prompt "Character sheet, full body standing pose and head-and-shoulders close-up portrait side by side of the same man: NURI, a 72-year-old man of North Aegean Mediterranean appearance, tall but slightly stooped, lean build; deeply lined weathered face with wind-reddened cheeks, short fully white-grey beard neatly trimmed close to the jaw, pale grey eyes, tired but warm expression; wearing a dark grey knitted wool beanie covering his hair, a thick cream cable-knit fisherman's sweater with a roll neck, a knee-length navy wool pea coat with two rows of brass buttons worn open, dark grey wool trousers, black knee-high rubber boots. In the full-body view he holds at his side by the handle an old brass hurricane lantern with a clear glass chimney and a wire carrying handle, tarnished and worn brass, unlit. Identical outfit in both views, plain neutral grey studio background, soft even frontal key light, no text, no labels, cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9" \
  --out projects/son-nobet/refs/nuri.png
```

### 2) refs/lamp_room.png — lamba odası establishing (1 kredi)

Karaktersiz. Fener duvar kancasında asılı (S8 sürekliliği). `--ref` ile Nuri sayfası →
fener görünümü ve film dokusu sabitlenir.

```bash
python3 scripts/genaipro.py image --n 4 --aspect 16:9 \
  --ref projects/son-nobet/refs/nuri.png \
  --prompt "Empty establishing shot, wide interior, no people: the lantern room at the top of an old white stone lighthouse with a black-painted iron cupola: an octagonal room walled in tall salt-streaked glass panes with black iron frames; at the centre a large honey-coloured Fresnel lens of stacked concentric glass prisms with a warm yellow-orange light turning inside it; brass fittings and rails, an iron floor with peeling grey-green paint; in one corner a brand-new plain white metal electrical cabinet with no labels and no text, one small green LED indicator light; an iron wall hook beside the stairwell hatch; a glass door opening onto a narrow circular outer gallery with a black iron railing, black sea far below, wind. Hanging on the iron wall hook is the same old brass hurricane lantern from the reference image, with a clear glass chimney and a wire carrying handle, tarnished and worn brass, unlit. Use the reference only for the lantern and the film look, do not include the man. night, cold steel-blue moonlight and deep navy shadows, the only warm light is amber-gold (#F2A541), strong warm-cold contrast, cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9" \
  --out projects/son-nobet/refs/lamp_room.png
```

### 3) refs/cape_night.png — burun gece + denizdeki ışık (1 kredi)

Karaktersiz. Kule tepesi lamba odasıyla eşleşsin diye `--ref lamp_room.png`.
`PROP_SEA_LIGHT` orta mesafede, kayalıkların önünde (S11–S13 ölçeğine yakın) yerleştirilir.

```bash
python3 scripts/genaipro.py image --n 4 --aspect 16:9 \
  --ref projects/son-nobet/refs/lamp_room.png \
  --prompt "Wide low-angle establishing shot, no people: a rocky North Aegean headland: dark grey wet rocks covered in seaweed running from the foot of a tall white stone lighthouse with a black iron cupola down into the sea, waves breaking over the rocks in white foam; a small arched wooden door at the base of the tower; a narrow dirt coastal path lined with dry pale grass curving inland away from the tower; open sea to the horizon. The lighthouse top matches the lantern room in the reference image, with the warm Fresnel light glowing inside. Navy-black sea, moon between clouds, the lighthouse beam sweeping across the water. A few metres off the rocks: a single softly glowing warm golden sphere of light hovering just above the sea surface, about the size of a human head, no flame, no object inside, smooth round glowing core with a soft diffuse halo, colour #FFD27A fading to amber #F2A541, reflected as a golden shimmer on the water below. night, cold steel-blue moonlight and deep navy shadows, the only warm light is amber-gold (#F2A541), strong warm-cold contrast, cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9" \
  --out projects/son-nobet/refs/cape_night.png
```

### 4) refs/stairwell.png — spiral merdiven, tepe kadraj (1 kredi)

Karaktersiz, S9 kadrajıyla aynı (top-down). Stil ve taş/beyaz badana dokusu için
`--ref lamp_room.png` + `cape_night.png`.

```bash
python3 scripts/genaipro.py image --n 4 --aspect 16:9 \
  --ref projects/son-nobet/refs/lamp_room.png projects/son-nobet/refs/cape_night.png \
  --prompt "Straight-down top shot, empty, no people: a narrow cast-iron spiral staircase winding down inside an old stone lighthouse tower, curved stone walls with flaking whitewash, one small vertical slit window letting in a shaft of cold blue moonlight across the iron steps, otherwise dark; seen from above the spiral narrows downward like the inside of a seashell. Same tower and film look as the reference images. night, cold steel-blue moonlight and deep navy shadows, the only warm light is amber-gold (#F2A541), strong warm-cold contrast, cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9" \
  --out projects/son-nobet/refs/stairwell.png
```

### 5) refs/cape_dawn.png — burun şafak (opsiyonel, 1 kredi)

S15–S16 için kule/patika geometrisini gece referansıyla eşler. Bütçe sıkışırsa atlanır;
o durumda S15/S16 anahtar kareleri doğrudan `cape_night.png` + `LIGHT_DAWN` ile üretilir.

```bash
python3 scripts/genaipro.py image --n 4 --aspect 16:9 \
  --ref projects/son-nobet/refs/cape_night.png \
  --prompt "Extreme wide establishing shot of the same place as the reference image at dawn, no people, no glowing sphere: a rocky North Aegean headland: dark grey wet rocks covered in seaweed running from the foot of a tall white stone lighthouse with a black iron cupola down into the sea, waves breaking over the rocks in white foam; a small arched wooden door at the base of the tower; a narrow dirt coastal path lined with dry pale grass curving inland away from the tower; open sea to the horizon. The lighthouse now shows a cold white electric light. early dawn, soft flat pale blue-grey light, overcast sky with a thin pale pink line on the horizon, no direct sun, quiet and cold, cinematic still, shot on 35mm film with anamorphic lens, soft organic film grain, subtle halation, oval bokeh, low-key naturalistic lighting, muted colour grade, photorealistic, highly detailed textures, 16:9" \
  --out projects/son-nobet/refs/cape_dawn.png
```

### Sıra ve bağımlılık

`nuri` → `lamp_room` → `cape_night` → `stairwell` → (`cape_dawn`)

Model: tümü varsayılan `nano_banana_pro` (referans tutarlılığı). Imagen 4 kullanılmaz —
`--ref` zinciri kritik.
