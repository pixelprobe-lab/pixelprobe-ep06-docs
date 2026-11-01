"""ELA 誤差等級分析與區塊雜訊圖 / Error Level Analysis + block noise map
用法 usage: python ela.py image.jpg out_prefix [quality=75]"""
import sys, io, numpy as np
from PIL import Image, ImageChops, ImageFilter
def ela(im, q=90, gain=20):
    b = io.BytesIO(); im.save(b, "JPEG", quality=q); b.seek(0); re = Image.open(b).convert("RGB")
    e = np.asarray(ImageChops.difference(im, re)).astype(np.float32).max(2); return np.clip(e * gain, 0, 255).astype(np.uint8)
def noise(im, blk=16):
    g = np.asarray(im.convert("L")).astype(np.float32); hp = g - np.asarray(im.convert("L").filter(ImageFilter.MedianFilter(3))).astype(np.float32)
    h, w = g.shape; out = np.zeros((h // blk, w // blk), np.float32)
    for y in range(h // blk):
        for x in range(w // blk): out[y, x] = hp[y * blk:(y + 1) * blk, x * blk:(x + 1) * blk].std()
    return out
def colorize(a):
    a = a.astype(np.float32); a = a / (np.percentile(a, 99.5) + 1e-6); a = np.clip(a, 0, 1)
    r = np.clip(a * 3, 0, 1); g = np.clip(a * 3 - 1, 0, 1); b = np.clip(a * 3 - 2, 0, 1)
    return Image.fromarray((np.dstack([r, g, b]) * 255).astype(np.uint8))
if __name__ == "__main__":
    im = Image.open(sys.argv[1]).convert("RGB"); o = sys.argv[2]; q = int(sys.argv[3]) if len(sys.argv) > 3 else 75
    colorize(ela(im, q)).save(o + "_ela.png")
    n = noise(im); colorize(n).resize(im.size, Image.NEAREST).save(o + "_noise.png"); np.save(o + "_noise.npy", n); print("ok")
