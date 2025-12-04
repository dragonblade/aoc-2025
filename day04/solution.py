import sys

adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

g = []
for l in sys.stdin:
    g.append(list(l.strip()))


def rem():
    ng = [row.copy() for row in g]
    s = 0
    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x] != "@":
                continue
            n = 0
            for dx, dy in adj:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(g[0]) and 0 <= ny < len(g):
                    if g[ny][nx] == "@":
                        n += 1
            if n < 4:
                ng[y][x] = "."
                s += 1
    return s, ng


t, g = rem()
print(t)
while True:
    u, g = rem()
    if u == 0:
        break
    t += u
print(t)
