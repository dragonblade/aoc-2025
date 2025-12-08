import math
import sys


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


jx = []
for l in sys.stdin:
    x, y, z = map(int, l.split(","))
    jx.append((x, y, z))

ps = []
for i in range(len(jx)):
    for j in range(i + 1, len(jx)):
        ps.append((i, j))

ps.sort(key=lambda p: dist(jx[p[0]], jx[p[1]]))

gs = {k: [k] for k in range(len(jx))}
sz = {k: k for k in range(len(jx))}
for p, q in ps[:1000]:
    if sz[p] != sz[q]:
        gp = sz[p]
        gq = sz[q]
        for v in gs[gq]:
            gs[gp].append(v)
            sz[v] = gp
        gs[gq] = []

ls = []
for k, v in gs.items():
    if len(v) > 0:
        ls.append(len(v))

a = 1
for v in sorted(ls, reverse=True)[:3]:
    a *= v
print(a)
