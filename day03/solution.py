import sys

a, b = 0, 0
for l in sys.stdin:
    l = l.strip()
    while len(l) > 2:
        n = 0
        for i in range(len(l)):
            c = l[:i] + l[i + 1 :]
            if int(c) > n:
                n = int(c)
        if len(str(n)) == 12:
            b += n
        elif len(str(n)) == 2:
            a += n
        l = str(n)

print(a, b)
