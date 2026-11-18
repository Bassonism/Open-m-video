import cv2, numpy as np, sys, json
vid, cum, out = sys.argv[1], np.load(sys.argv[2]), sys.argv[3]
TOP0, PITCH, H = 1187, 536, 533
COLS = [(0,400),(403,803),(806,1206)]
cmax = cum.max(); rows = []
k = 0
while TOP0 + PITCH*k + H <= 2622 + cmax - 5:
    T = TOP0 + PITCH*k
    best = min(range(len(cum)), key=lambda f: abs((T - cum[f]) - 1300) if 500 <= T-cum[f] <= 2622-H-8 else 1e9)
    rows.append((k, best, T - cum[best])); k += 1
cap = cv2.VideoCapture(vid); need = {}
for k,f,y in rows: need.setdefault(f, []).append((k,y))
idx = 0; meta = []
while need:
    ok, fr = cap.read()
    if not ok: break
    if idx in need:
        g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY).astype(float); rs = g[:, 20:1186].std(axis=1)
        for k, y in need.pop(idx):
            y = int(round(y))
            # snap: find gap row just above tile top
            cand = [yy for yy in range(y-20, y+20) if rs[yy] < 6]
            if cand:
                gy = min(cand, key=lambda yy: abs(yy-(y-2))); 
                # last row of this gap group
                while gy+1 < 2622 and rs[gy+1] < 6: gy += 1
                y = gy + 1
            for c,(x0,x1) in enumerate(COLS):
                n = k*3 + c + 1
                cv2.imwrite(f"{out}/{n:03d}.jpg", fr[y:y+H, x0:x1], [cv2.IMWRITE_JPEG_QUALITY, 95])
                meta.append({"n": n, "row": k, "col": c, "frame": idx, "y": y, "snapped": bool(cand)})
    idx += 1
json.dump(sorted(meta, key=lambda m: m["n"]), open(f"{out}/meta.json","w"), indent=0)
print("rows", len(rows), "tiles", len(meta), "unsnapped", sum(not m["snapped"] for m in meta)//3)
