"""讀 PDF 中繼資料與存檔次數 / read PDF metadata and count saves (incremental updates)"""
import sys, re, json
from pypdf import PdfReader
def check(p):
    r = PdfReader(p); m = {k: str(v) for k, v in (r.metadata or {}).items()}
    raw = open(p, "rb").read(); eofs = len(re.findall(rb"%%EOF", raw))
    return {"metadata": m, "eof_markers": eofs, "note_zh": "EOF 超過 1 個 = 存檔後又被增量更新過（不代表一定造假）", "note_en": ">1 %%EOF = updated after first save (not proof of forgery)"}
if __name__ == "__main__": print(json.dumps(check(sys.argv[1]), ensure_ascii=False, indent=1))
