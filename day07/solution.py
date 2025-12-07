import sys

g = []
for l in sys.stdin:
    g.append(list(l))

a = 0
s = [g[0].index("S")]
for i in range(1, len(g)):
    n = set()
    for x in s:
        if g[i][x] == ".":
            n.add(x)
        elif g[i][x] == "^":
            a += 1
            n.add(x - 1)
            n.add(x + 1)
    s = n
print(a)

t = {g[0].index("S"): 1}
for i in range(1, len(g)):
    n = {k: 0 for k in range(len(g[0]))}
    for x in t:
        if g[i][x] == ".":
            n[x] += t[x]
        elif g[i][x] == "^":
            n[x - 1] += t[x]
            n[x + 1] += t[x]
    t = n
print(sum(t.values()))
