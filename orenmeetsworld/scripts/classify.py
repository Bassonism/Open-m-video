import cv2, numpy as np, json, sys
d = sys.argv[1]; meta = json.load(open(f"{d}/meta.json"))
def mask(n, dx=0, dy=0):
    t = cv2.imread(f"{d}/{n:03d}.jpg"); g = cv2.cvtColor(t[18+dy:78+dy, 322+dx:382+dx], cv2.COLOR_BGR2GRAY)
    return g > 225
T = {"reel": mask(4), "carousel": mask(5), "pinned": mask(1)}
def iou(a,b): return (a&b).sum()/max((a|b).sum(),1)
res = {}
for m in meta:
    n = m["n"]; best = ("none", 0)
    for dx in (-3,0,3):
        for dy in (-3,0,3):
            mm = mask(n,dx,dy)
            for k,t in T.items():
                s = iou(mm,t)
                if s > best[1]: best = (k, s)
    res[n] = (best[0] if best[1] > 0.45 else "none", round(best[1],2))
json.dump(res, open(f"{d}/types.json","w"))
print([ (n,)+res[n] for n in range(1,25)])
from collections import Counter; print(Counter(v[0] for v in res.values()))
