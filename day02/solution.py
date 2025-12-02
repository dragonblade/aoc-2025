import math

t = []
r = input().split(",")
for q in r:
    a, b = map(int, q.split("-"))
    if a >= b:
        continue
    t += [(a, b)]
l = max(b for _, b in t)

x, y = 0, 0
v = set()
c = 1
while int(f"{c}{c}") <= l:
    d = 2
    while int("".join([str(c)] * d)) <= l:
        n = int("".join([str(c)] * d))
        for a, b in t:
            if d == 2 and a <= n <= b:
                x += n
            if a <= n <= b and n not in v:
                y += n
                v.add(n)
                break
        d += 1
    c += 1

print(x, y)
