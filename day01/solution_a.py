import sys

s = 0
d = 50
for l in sys.stdin:
    r = l[0]
    c = int(l[1:])
    if r == "L":
        d -= c
    else:
        d += c
    d %= 100
    if d == 0:
        s += 1

print(s)
