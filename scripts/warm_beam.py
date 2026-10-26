#!/usr/bin/env python3
"""Bir karedeki soğuk fener huzmesini amber (#F2A541 ailesi) tona çeker — kredisiz renk düzeltmesi.

Kullanım:
    python3 -I scripts/warm_beam.py <girdi.png> <çıktı.png> X Y G Y  (kutu: sol üst köşe + genişlik/yükseklik)

Yalnızca kutunun içindeki parlak pikseller, parlaklıkları korunarak amber'e çekilir. Varsayılan
kare boyutu 1376x768 (genaipro Nano Banana 16:9 çıktısı).
"""
import subprocess
import sys

W, H = 1376, 768


def main():
    src, dst = sys.argv[1], sys.argv[2]
    x, y, w, h = map(int, sys.argv[3:7])
    raw = bytearray(subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True).stdout)
    for j in range(y, y + h):
        for i in range(x, x + w):
            k = (j * W + i) * 3
            r, g, b = raw[k], raw[k + 1], raw[k + 2]
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            t = max(0.0, min(1.0, (lum - 55) / 60.0))
            if t <= 0:
                continue
            tr, tg, tb = lum * 1.45, lum * 1.12, lum * 0.62  # aynı parlaklıkta amber hedef
            raw[k] = min(255, int(r + (tr - r) * t))
            raw[k + 1] = min(255, int(g + (tg - g) * t))
            raw[k + 2] = max(0, int(b + (tb - b) * t))
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{W}x{H}", "-i", "-", dst],
        input=bytes(raw), check=True)


if __name__ == "__main__":
    main()
