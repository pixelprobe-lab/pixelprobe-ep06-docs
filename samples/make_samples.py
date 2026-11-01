"""EP6 合成示範樣本產生器 / synthetic demo sample generator
全部虛構：雲杉銀行 Cedar Bank、星橋貿易、海帆國際、小林都是編造的名稱；每張圖都有「合成示範 SYNTHETIC DEMO」浮水印。
All names are invented. Every image carries a SYNTHETIC DEMO watermark. For verification teaching only."""
import os, sys, json, io
from PIL import Image, ImageDraw, ImageFont
O = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "out")
os.makedirs(O, exist_ok=True)
CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"; CJKB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
ODD = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"   # 不同字型（示範用）/ a different font, for the demo
def f(s, b=False): return ImageFont.truetype(CJKB if b else CJK, s, index=2)
W, H = 750, 1500; TEAL = (22, 96, 86); CARD = (243, 246, 249); GRAY = (110, 118, 128)
def mark(im):
    d = ImageDraw.Draw(im); t = "合成示範 SYNTHETIC DEMO"; fn = f(22, True)
    w = d.textlength(t, font=fn); d.rounded_rectangle([W - w - 36, H - 60, W - 12, H - 20], 10, fill=(255, 235, 59)); d.text((W - w - 24, H - 40), t, font=fn, fill=(0, 0, 0), anchor="lm")
def transfer(amount="15,000", ttime="23:40", status="23:41"):
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    d.text((40, 32), status, font=f(30, True), fill=(20, 20, 20), anchor="lm"); d.rounded_rectangle([640, 20, 700, 44], 5, outline=(20, 20, 20), width=3); d.rectangle([645, 25, 685, 39], fill=(20, 20, 20))
    d.rectangle([0, 64, W, 170], fill=TEAL); d.polygon([(60, 145), (90, 85), (120, 145)], fill=(255, 255, 255)); d.rectangle([86, 145, 94, 158], fill=(255, 255, 255))
    d.text((140, 117), "雲杉銀行  Cedar Bank", font=f(40, True), fill=(255, 255, 255), anchor="lm")
    d.ellipse([315, 220, 435, 340], fill=(46, 170, 90)); d.line([(343, 282), (367, 306), (410, 255)], fill=(255, 255, 255), width=12)
    d.text((W / 2, 385), "轉帳成功", font=f(48, True), fill=(20, 20, 20), anchor="mm"); d.text((W / 2, 435), "Transfer successful", font=f(26), fill=GRAY, anchor="mm")
    d.rounded_rectangle([40, 480, W - 40, 640], 24, fill=CARD)
    d.text((80, 575), "NT$", font=f(44, True), fill=(20, 20, 20), anchor="ls"); d.text((180, 575), amount, font=f(84, True), fill=(20, 20, 20), anchor="ls")
    rows = [("轉出帳戶", "海帆國際  ****1234"), ("轉入帳戶", "星橋貿易  ****5678"), ("手續費", "NT$ 15"), ("轉帳前餘額", "NT$ 52,310"),
            ("轉帳後餘額", "NT$ 37,295"), ("交易時間", f"2026/03/15 (日) {ttime}"), ("交易序號", "CB2603152340-0417")]
    for i, (a, b) in enumerate(rows):
        y = 700 + i * 92; d.text((60, y), a, font=f(32), fill=GRAY, anchor="lm"); d.text((W - 60, y), b, font=f(32, True), fill=(20, 20, 20), anchor="rm")
        d.line([(60, y + 46), (W - 60, y + 46)], fill=(228, 232, 236), width=2)
    d.rounded_rectangle([60, 1360, W - 60, 1440], 40, fill=TEAL); d.text((W / 2, 1400), "完成  Done", font=f(34, True), fill=(255, 255, 255), anchor="mm")
    mark(im); return im
def jpeg(im, q=90):
    b = io.BytesIO(); im.save(b, "JPEG", quality=q); b.seek(0); return Image.open(b).convert("RGB")
# 原圖：截圖存成 JPEG（像一般轉傳）/ original, saved as JPEG like a typical forwarded image
orig = jpeg(transfer(), 75)   # 轉傳時被壓成 q75 / forwarded at q75
# 示範修改：金額與時間被局部重畫（不同字型、無抗鋸齒、底色略不同、基線偏移），再存一次 JPEG
# Demo edit: amount & time patched (different font, no anti-aliasing, slightly different fill, shifted baseline), then re-saved
ed = orig.copy(); d = ImageDraw.Draw(ed); d.fontmode = "1"
AM = (176, 492, 520, 600); d.rectangle(AM, fill=(248, 249, 251)); d.text((182, 579), "48,000", font=ImageFont.truetype(ODD, 80), fill=(30, 30, 30), anchor="ls")
TM = (598, 1138, 694, 1180); d.rectangle(TM, fill=(253, 253, 253)); d.text((690, 1158), "23:52", font=ImageFont.truetype(ODD, 31), fill=(30, 30, 30), anchor="rm")
d.fontmode = "L"; edited = jpeg(ed, 95)   # 修改後另存 q95 / re-saved at q95
orig.save(f"{O}/transfer_original.jpg", quality=95); edited.save(f"{O}/transfer_edited.jpg", quality=95)
edited.save(f"{O}/transfer_edited.png")
# 對話截圖 / chat screenshot (invented app "Mori Chat", not modeled on any real app)
def chat():
    im = Image.new("RGB", (W, H), (236, 233, 246)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 150], fill=(88, 64, 160)); d.text((40, 32), "23:51", font=f(30, True), fill=(255, 255, 255), anchor="lm")
    d.ellipse([40, 76, 104, 140], fill=(255, 196, 120)); d.text((72, 108), "林", font=f(30, True), fill=(80, 50, 0), anchor="mm")
    d.text((124, 96), "小林（海帆國際）", font=f(34, True), fill=(255, 255, 255), anchor="lm"); d.text((124, 132), "Mori Chat · 新聯絡人 new contact", font=f(22), fill=(220, 210, 255), anchor="lm")
    y = 200
    def bub(text, tm, me=False, h=90, img=None):
        nonlocal y; fn = f(32); w = int(d.textlength(text, font=fn)) + 60 if not img else 300
        x0 = W - 40 - w if me else 40; d.rounded_rectangle([x0, y, x0 + w, y + h], 28, fill=(255, 255, 255) if not me else (196, 236, 210))
        if img: th = img.resize((150, 300)); im.paste(th, (x0 + 75, y + 15))
        else: d.text((x0 + 30, y + h / 2), text, font=fn, fill=(20, 20, 20), anchor="lm")
        d.text((x0 + w + 12, y + h - 10) if not me else (x0 - 12, y + h - 10), tm, font=f(22), fill=GRAY, anchor="ls" if not me else "rs"); y += h + 36
    bub("你好，款項已經轉過去了", "23:42"); bub("", "23:42", h=330, img=edited)
    d.rounded_rectangle([40, y, 440, y + 110], 24, fill=(255, 255, 255)); d.rectangle([66, y + 20, 128, y + 90], fill=(220, 60, 60)); d.text((97, y + 55), "PDF", font=f(22, True), fill=(255, 255, 255), anchor="mm")
    d.text((148, y + 40), "轉帳證明.pdf", font=f(30, True), fill=(20, 20, 20), anchor="lm"); d.text((148, y + 80), "86 KB", font=f(22), fill=GRAY, anchor="lm"); d.text((452, y + 100), "23:43", font=f(22), fill=GRAY, anchor="ls"); y += 146
    bub("麻煩今天一定要出貨，謝謝！", "23:45"); bub("收到，我先確認一下", "23:50", me=True)
    mark(im); return im
chat().save(f"{O}/chat.png")
# PDF：第一版正常存檔，之後「增量更新」改內容並改 metadata → 檔案內有兩段 EOF
# PDF: saved once, then an incremental update edits it → two %%EOF markers, ModDate ≠ CreationDate
from pypdf import PdfReader, PdfWriter
p1 = f"{O}/_v1.pdf"; orig.save(p1, "PDF", resolution=150)
w = PdfWriter(clone_from=p1); w.add_metadata({"/Title": "Transfer receipt (synthetic demo)", "/Producer": "CedarDocs Export 3.2 (synthetic)", "/CreationDate": "D:20260315234100+08'00'", "/ModDate": "D:20260315234100+08'00'"})
w.write(f"{O}/_v1b.pdf")
w2 = PdfWriter(f"{O}/_v1b.pdf", incremental=True)
ov = f"{O}/_ov.pdf"; edited.save(ov, "PDF", resolution=150); w2.pages[0].merge_page(PdfReader(ov).pages[0], over=True)
w2.add_metadata({"/ModDate": "D:20260317101500+08'00'", "/Producer": "QuickPDF Editor 9 (synthetic)"}); w2.write(f"{O}/transfer_receipt.pdf")
for x in ("_v1.pdf", "_v1b.pdf", "_ov.pdf"): os.remove(f"{O}/{x}")
json.dump({"amount_box": AM, "time_box": TM, "size": [W, H]}, open(f"{O}/boxes.json", "w"))
print("ok", O)
