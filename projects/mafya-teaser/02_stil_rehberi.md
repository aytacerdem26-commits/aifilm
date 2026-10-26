# HESAP (teaser) — Stil Rehberi

> Kaynak: `00_brief.md`, `01_senaryo.md` (rev. 2, çatışmalı, onaylı). Bu dosyadaki İngilizce
> bloklar (`STYLE_SUFFIX`, `LIGHT_*`, `CHAR_*`, `LOC_*`, `PROP_*`, `NEG`) bütün görsel ve video
> prompt'larında **kelimesi kelimesine** kopyalanır; kısaltılmaz, yeniden yazılmaz.
> Önerilen prompt sırası: `[kadraj + aksiyon] + CHAR_* + LOC_* (+ STATE) + PROP_* + LIGHT_* + STYLE_SUFFIX`.

---

## 1. Görsel stil

- **Tür:** Sinematik gerçekçi suç dramı. Şık, karanlık, ağır; dizi teaser'ı kalitesinde ama
  "reklam parlaklığı" yok.
- **Format:** 35mm film hissi, **sferik lens** (anamorfik DEĞİL: oval bokeh yok, yatay flare
  yok; yuvarlak bokeh). İnce organik film grain, hafif halation (lamba ve neon çevresinde).
- **Kontrast:** Yüksek. Derin siyahlar, ışık yalnızca yüzlere, ellere ve masaya düşer.
  Gölgelerde hafif mavi-teal detay kalır, siyahlar tamamen ezilmez.
- **Atmosfer:** Havada ince sigara dumanı ve toz (ışık huzmesini görünür kılar). Çatışma
  sonrasında barut dumanı + toz yoğunlaşır, havada cam kırıntıları parlar.
- **Doku:** Eski koyu ahşap, buğulu cam, keten örtü, yün takım, deri ceket. Yüzeyler mat ve
  dokunsal; plastik/CGI parlaklığı yok, cilt gözenekleri ve kırışıklar görünür.

## 2. Renk paleti ve ışık

| Rol | Renk | Hex |
|---|---|---|
| Gölge / boşluk | Mürekkep siyahı | `#0A0A0D` |
| Ahşap / orta tonlar | Koyu ceviz kahve | `#3B2416` |
| Tungsten lamba (Rıza'nın düzeni) | Sıcak tungsten sarısı | `#E8A33D` |
| Vitrin dışı neon — sıcak | Neon kırmızı | `#D7263D` |
| Vitrin dışı neon — soğuk / gölge dolgusu | Neon mavi | `#2B59C3` |
| Baskın: far ışığı / namlu alevi | Sert soğuk beyaz | `#EEF3FF` |

**Işık yaklaşımı**
- **Ana ışık (anahtar):** Masanın üstünde alçak sarkan tek tungsten lamba; tepeden, dar
  koni. Yüzlerin üst yarısı sıcak sarı, alt kısımlar gölgede. Göz çukurları koyu.
- **Kontra / kenar ışık:** Rıza'nın arkasındaki buğulu vitrinden kırmızı ve mavi neon
  parıltısı (tabela ve yazı **asla** görünmez; sadece renkli ışık lekesi ve buğu). Saç ve
  omuz kenarlarında kırmızı/mavi çizgi.
- **Çekim 1 (gerilim):** Sadece tungsten + neon. Sakin, durağan.
- **Çekim 2–6 (baskın ve sonrası):** Vitrinden giren sert beyaz far ışığı devreye girer;
  dumanda huzme oluşturur. Namlu alevleri beyaz anlık çakmalar. Lamba sallanır → ışık yüzde
  gelip gider.
- Ten rengi tungsten altında doğal sıcak kalır; neon yüzün yalnızca kenarına vurur, yüzü
  maviye/kırmızıya boğmaz.

## 3. Kamera dili (dikey 9:16)

- **Lens:** Sferik prime. Yakın planlar 50–85mm, orta planlar 35–50mm. Geniş açı yok
  (dikeyde mekân üstten-alta dar dilim olarak okunur).
- **Derinlik:** Sığ alan derinliği (f/1.8–2.8). Odak yüzde/gözde; ön plan (bardak, silah)
  ve arka plan (raflar, vitrin) yuvarlak bokeh ile flu.
- **Kompozisyon:** Dikey kadrajı yüz + eller dolduruyor. Yüz üst üçte birde, eller/masa alt
  üçte birde. Dar, sıkışık kadraj; boş gökyüzü/tavan yok. Altyazı ortada okunacağı için
  kadrajın orta bandında kritik detay (göz, ağız) yerine yüz biraz yukarıda tutulur.
- **Hareket:** Çekim 1 ve 6: neredeyse durağan, çok yavaş push-in. Çekim 2–5: hafif el
  kamerası titremesi, kısa sarsıntı, ama hızlı pan/whip yok. Drone, vinç, 360° dönüş yok.
- **Açı:** Göz hizası (1), yere yakın alçak açı (4, 6). Çekim 6 Rıza'nın bakış açısından
  alttan yukarı.

## 4. Sabit İngilizce bloklar

### STYLE_SUFFIX (her prompt'un sonuna, tek satır)

```
cinematic crime drama still, shot on 35mm film with spherical prime lens, shallow depth of field, round bokeh, fine organic film grain, subtle halation, high contrast low-key lighting, warm tungsten amber key light with red and blue neon rim light, thin haze of smoke and dust in the air, deep blacks, photorealistic, realistic skin texture, vertical 9:16 composition, no text, no watermark, no logo
```

### NEG (negatif prompt / "avoid" satırı; destekleyen her çağrıda)

```
no blood, no wounds, no gore, no bodies, no readable text, no signage letters, no logos, no brand names, no watermark, no anamorphic lens flare, no cartoon, no CGI look
```

### Işık blokları (STYLE_SUFFIX'ten hemen önce, sahneye göre biri)

`LIGHT_CALM` (çekim 1, referanslar):
```
night, a single low-hanging tungsten lamp above the table casting a narrow warm amber cone, soft red and blue neon glow seeping through a fogged window behind, everything else falls into deep shadow
```

`LIGHT_RAID` (çekim 2–6):
```
night, harsh cold white car headlight beams cutting through the broken front window into thick smoke and dust, the tungsten lamp above swinging and flickering, red and blue neon glow at the edges, sharp light-and-shadow contrast
```

### CHAR_RIZA

```
RIZA, a 66-year-old Turkish man, broad-shouldered and slightly heavy-set; short fully silver-white hair, a neatly trimmed short white beard, deep horizontal forehead lines, heavy hooded eyelids, dark brown eyes, a thin old pale scar cutting vertically through his left eyebrow; calm, cold, unreadable expression; wearing a charcoal grey wool three-piece suit with matching waistcoat, a crisp white dress shirt with no tie and the top button open, a dark burgundy pocket square in the breast pocket
```

Notlar: Gözlük, yüzük, saat, kolye, şapka **yok**. Ceket hep giyili, yelek düğmeli.
Çatışma sonrası (çekim 4–6) blok sonuna aynen eklenir:
`, fine dust and tiny glass shards on his hair and shoulders`

### CHAR_KENAN

```
KENAN, a 34-year-old Turkish man, lean and athletic; short black hair slicked straight back, a short black two-to-three-day stubble beard, sharp high cheekbones, light brown eyes, a single short shaved line cut into the hair just above his right ear; alert, controlled expression; wearing a black leather jacket over a black fitted turtleneck sweater
```

Notlar: Takı, saat, dövme, gözlük **yok**. Ceket hep giyili, fermuarı/önü açık.
Silah elindeyse `PROP_PISTOL` ayrıca eklenir. Çatışma sonrası (çekim 4–6) blok sonuna:
`, fine dust and tiny glass shards on his hair and shoulders`

### LOC_MEYHANE

```
the interior of an old closed-for-the-night Istanbul meyhane tavern, dark carved wooden wall panelling, wooden shelves on the back wall lined with empty raki and wine bottles, other tables in the background with chairs turned upside down on them; a single set table in the centre with a white linen tablecloth, two tall slim raki glasses, an open raki bottle with no label text, small meze plates, a glass ashtray with a thin curl of cigarette smoke; a large fogged shop window behind the table glowing with diffuse red and blue neon light from outside, no visible sign and no lettering
```

`LOC_MEYHANE_AFTER` (çekim 3 sonu – 6; LOC_MEYHANE yerine kullanılır):
```
the interior of an old Istanbul meyhane tavern after a raid, dark carved wooden wall panelling, shattered bottles on the back wall shelves, the central table knocked over on its side, the white linen tablecloth on the floor, broken glass and wood splinters scattered across the floor, the large front window shattered, gunpowder smoke and dust hanging in the air, no visible sign and no lettering
```

### PROP_PISTOL

```
a black matte semi-automatic pistol, plain and unbranded, no engravings, no markings
```

Masada (çekim 1, referans): `lying on its side in the centre of the table` eklenir.
Elde (çekim 4–6): `held in Kenan's right hand` eklenir. Prompt'larda "shoot, kill, aim at"
kelimeleri kullanılmaz; yerine "holding a pistol, raises the pistol, muzzle flash".

## 5. Kaçınılacaklar

- Kan, yara, kesik, ceset, acı çeken yüz; vurulma anının kendisi.
- Gerçek bir dizi, film, marka veya kişiye benzerlik (ünlü oyuncu yüzü, bilinen dizi
  kostümü/afiş kompozisyonu). Şişelerde okunur etiket yok.
- Tabelada, vitrinde, şişede, duvarda **herhangi bir yazı/harf**; neon yalnızca renkli ışık.
- Filigran, logo, altyazı, UI öğesi (altyazı kurguda eklenir).
- Anamorfik görünüm (oval bokeh, yatay mavi flare), letterbox siyah bantlar.
- Aşırı doygun "neon-punk/cyberpunk" görünüm; yüz tamamen mor/mavi.
- Karakter bloklarından sapma: Rıza'da kravat, Kenan'da renkli kıyafet, gözlük, takı;
  Rıza'nın kaşındaki yara izinin sağa kayması, Kenan'ın traş çizgisinin sola kayması.
- Silahın markalı/gravürlü görünmesi; birden fazla silah (baskıncılar hariç, onlar siluet).

## 6. Referanslar

| Blok | Dosya | Kaynak / not |
|---|---|---|
| `CHAR_RIZA` | `refs/riza.png` | Görev `aa9d1571`, varyant 2 (nano_banana_pro, 9:16). Belden yukarı, cepheden. Yara izi **sol kaşta** (görüntüde sağda) doğru taraf, ama ince ve az belirgin. Prompt'ta yara izi her zaman açıkça yazılmalı. |
| `CHAR_KENAN` | `refs/kenan.png` | Görev `a8896e9e`, varyant 2, `--ref riza.png`. **Yatay aynalandı** (`-flop`): 4 varyantın hepsinde traş çizgisi sol kulağın üstündeydi, aynalamayla sağ kulağa geçti. Orijinali `refs/alts/kenan_v2.png`. |
| `LOC_MEYHANE` + `PROP_PISTOL` | `refs/meyhane.png` | Görev `5c95f92e`, varyant 3, `--ref riza.png`. Ortada masa, yan yatan tabanca, iki rakı bardağı, etiketsiz şişe, dumanlı kül tablası; arkada buğulu vitrin ve kırmızı/mavi neon. Vitrindeki harf benzeri neon lekesi yerel bulanıklaştırmayla silindi. Orijinali `refs/alts/meyhane_v3.png`. |

Notlar:
- İndirilen dosyalar `.png` uzantılı ama içerik **JPEG**. Araçlar için sorun değil, ama format kontrolü yapan bir adım olursa bunu bilin.
- Diğer varyantlar `refs/alts/` altında. Görev kayıtları `refs/genaipro_tasks.jsonl` dosyasında (`fetch` ile kredisiz yeniden indirilebilir).
- Referans görsellerinde çatışma sonrası hâl (toz, cam, devrik masa) **yok**. Bu hâl prompt'a `LOC_MEYHANE_AFTER` ve toz eki ile eklenir.
