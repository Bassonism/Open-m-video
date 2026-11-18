"""Usage: python3 -I grab.py <shortcodes_or_urls.txt> <out_dir>
For each Instagram post: saves first image (carousel cover) + writes headlines.xlsx/csv."""
import sys, re, html, base64, csv, time, os, requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
src, out = sys.argv[1], sys.argv[2]
os.makedirs(f"{out}/images", exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}
codes = []
for line in open(src):
    m = re.search(r"(?:/p/)?([A-Za-z0-9_-]{9,})/?\s*$", line.strip())
    if m and m.group(1) not in codes: codes.append(m.group(1))
def meta(page, prop):
    m = re.search(r'property="og:%s" content="([^"]*)"' % prop, page) or re.search(r'content="([^"]*)" property="og:%s"' % prop, page)
    return html.unescape(m.group(1)) if m else ""
rows = []
for i, c in enumerate(codes, 1):
    url = f"https://www.instagram.com/p/{c}/"
    row = {"#": i, "shortcode": c, "url": url, "date": "", "is_carousel": "", "headline": "", "full_caption": "", "image_file": "", "status": ""}
    try:
        page = requests.get(url, headers=UA, timeout=30).text
        img, title, desc = meta(page, "image"), meta(page, "title"), meta(page, "description")
        cap = re.sub(r'^.*? on Instagram: "', "", title).rstrip('"')
        d = re.search(r"on ([A-Z][a-z]+ \d{1,2}, \d{4})", desc)
        row["date"] = d.group(1) if d else ""
        row["full_caption"] = cap
        row["headline"] = next((l.strip() for l in cap.splitlines() if l.strip()), "")
        efg = re.search(r"efg=([^&]+)", img)
        try: tag = base64.b64decode(efg.group(1) + "==").decode(errors="ignore") if efg else ""
        except Exception: tag = ""
        row["is_carousel"] = "yes" if "CAROUSEL" in tag else ("no" if tag else "unknown")
        if title.strip() == "Instagram" or "cdninstagram" not in img:
            row["status"] = "blocked: Instagram returned generic/login page"; img = ""
        if img:
            r = requests.get(img, headers=UA, timeout=60); r.raise_for_status()
            fn = f"{i:03d}_{c}.jpg"; open(f"{out}/images/{fn}", "wb").write(r.content)
            row["image_file"] = f"images/{fn}"; row["status"] = "ok"
        elif not row["status"]: row["status"] = "no image (login wall?)"
    except Exception as e:
        row["status"] = f"error: {type(e).__name__}: {str(e)[:120]}"
    rows.append(row); print(i, c, row["is_carousel"], row["status"], "|", row["headline"][:70], flush=True)
    time.sleep(2)
cols = list(rows[0].keys()) if rows else []
with open(f"{out}/headlines.csv", "w", newline="") as f:
    w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(rows)
wb = Workbook(); ws = wb.active; ws.title = "Headlines"
ws.append(cols + ["preview"])
for r in rows:
    ws.append([r[k] for k in cols])
    if r["image_file"]:
        try:
            im = XLImage(f"{out}/{r['image_file']}"); im.width, im.height = 120, 150
            ws.add_image(im, f"J{ws.max_row}"); ws.row_dimensions[ws.max_row].height = 115
        except Exception: pass
    ws.cell(ws.max_row, 3).hyperlink = r["url"]
for col, wdt in zip("ABCDEFGHIJ", [5, 14, 40, 18, 11, 60, 80, 24, 22, 18]): ws.column_dimensions[col].width = wdt
ws.freeze_panes = "A2"; wb.save(f"{out}/headlines.xlsx")
print("done", len(rows))
