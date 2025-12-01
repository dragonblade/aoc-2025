import sys

s = 0
d = 50
for l in sys.stdin:
    r = l[0]
    c = int(l[1:])
    if r == "L":
        for _ in range(c):
            d -= 1
            if d < 0:
                d = 99
            if d == 0:
                s += 1
    else:
        for _ in range(c):
            d += 1
            if d >= 100:
                d = 0
            if d == 0:
                s += 1

print(s)
