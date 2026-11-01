# PixelProbe EP06 · 轉帳了嗎？ Paid or Not?

照妖鏡實驗室 EP06 示範程式碼：檢查可疑的轉帳截圖與 PDF。
Demo code for PixelProbe EP06: checking a suspicious transfer screenshot and PDF.

> ⚠️ 所有圖片與名稱都是自製合成示範（雲杉銀行、海帆國際、星橋貿易皆為虛構）。
> All images and names are self-made synthetic demos. Results are **leads, not proof**.

## 內容 Contents
- `samples/make_samples.py` — 產生合成截圖、聊天畫面、PDF / builds the synthetic screenshot, chat and PDF
- `checks/pdf_meta.py` — 讀 PDF metadata、數 `%%EOF` / reads PDF metadata and counts `%%EOF` markers
- `checks/ela.py` — ELA 誤差等級分析與雜訊圖 / Error Level Analysis and noise map

## 使用 Usage
```bash
pip install pillow numpy pypdf
python samples/make_samples.py
python checks/pdf_meta.py out/transfer_receipt.pdf
python checks/ela.py out/transfer_edited.jpg out/edited 75
```

## 限制 Limits
重新截圖、多次壓縮會洗掉痕跡；metadata 可被清除；真實截圖也可能有類似瑕疵。最可靠的方法是登入自己的帳戶或向銀行確認。
Re-screenshots and recompression erase traces; metadata can be stripped; genuine images can show similar quirks. Always confirm with your own bank account.
