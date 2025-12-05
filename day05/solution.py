import sys

r, s = [], []
for l in sys.stdin:
    if "-" in l:
        a, b = l.strip().split("-")
        r.append((int(a), int(b)))
    elif len(l.strip()) > 0:
        s.append(int(l.strip()))

a = 0
for n in s:
    f = False
    for x, y in r:
        if x <= n <= y:
            f = True
            break
    if f:
        a += 1
print(a)

while True:
    e = False
    for i in range(len(r)):
        x, y = r[i]
        for j in range(len(r)):
            if i == j:
                continue
            v, w = r[j]
            if x <= v <= y or x <= w <= y:
                r[i] = (min(x, v), max(y, w))
                r.pop(j)
                e = True
                break
        else:
            continue
        break
    if not e:
        break

b = 0
for x, y in r:
    b += y - x + 1
print(b)
