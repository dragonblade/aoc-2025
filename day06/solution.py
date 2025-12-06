import sys

g = []
for l in sys.stdin:
    g.append(list(l))

p = []
for l in g:
    l = "".join(l).split()
    for i, v in enumerate(l):
        if len(p) <= i:
            p.append([])
        p[i].append(v)

a = 0
for col in p:
    op = col[-1]
    if op == "+":
        s = 0
        for v in col[:-1]:
            s += int(v)
    elif op == "*":
        s = 1
        for v in col[:-1]:
            s *= int(v)
    a += s
print(a)

b = 0
r = []
for i in reversed(range(len(g[0]))):
    x = ("".join(l[i] for l in g)).strip()
    if not x:
        continue
    elif x[-1] == "+":
        r.append(x[:-1])
        s = 0
        for v in r:
            s += int(v)
        b += s
        r.clear()
    elif x[-1] == "*":
        r.append(x[:-1])
        s = 1
        for v in r:
            s *= int(v)
        b += s
        r.clear()
    else:
        r.append(x)
print(b)
