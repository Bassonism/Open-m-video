import cv2, numpy as np, sys
cap = cv2.VideoCapture(sys.argv[1]); out = sys.argv[2]
def strip(f): return cv2.cvtColor(f[1300:2550, 50:1150], cv2.COLOR_BGR2GRAY).astype(np.float32)
prev = None; cum = []; c = 0.0; resps = []
while True:
    ok, f = cap.read()
    if not ok: break
    s = strip(f)
    if prev is not None:
        (dx, dy), r = cv2.phaseCorrelate(prev, s); c -= dy; resps.append(r)
    cum.append(c); prev = s
np.save(f"{out}/cum.npy", np.array(cum))
print("n", len(cum), "total scroll", round(c), "min resp", round(min(resps),3), "low-resp frames", sum(r<0.2 for r in resps))
