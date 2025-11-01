from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1000000)
    data = list(map(int, sys.stdin.read().strip().split()))
    i = 0
    n = data[i]; i += 1

    sl = []
    for _ in range(n):
        sl.append(data[i:i+4])
        i += 4

    sx, sy, e = data[i:i+3]

    # Graph structures
    g = defaultdict(list)
    nx = dict()

    # Build structures
    for s in range(n):
        x1, y1, x2, y2 = sl[s]
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        L = abs(x2 - x1)

        if dy == -1:
            for k in range(L):
                x = x1 + dx * k
                y = y1 - k
                g[(x, y)].append(s)
                nx[(x, y, s)] = (x + dx, y - 1)
            g[(x2, y2)].append(s)
        else:
            for k in range(L):
                x = x2 - dx * k
                y = y2 - k
                g[(x, y)].append(s)
                nx[(x, y, s)] = (x - dx, y - 1)
            g[(x1, y1)].append(s)

    def fall(x, y):
        """Find the nearest point below (x, y) that exists in g."""
        for yy in range(y - 1, -1, -1):
            if (x, yy) in g:
                return (x, yy)
        return (x, 0)

    x, y = sx, sy

    # Adjust to nearest valid point
    if (x, y) not in g:
        x, y = fall(x, y)

    while True:
        if y == 0:
            break

        if (x, y) not in g:
            x, y = fall(x, y)
            continue

        ids = g[(x, y)]

        if len(ids) == 1:
            s = ids[0]
            if (x, y, s) not in nx:
                x, y = fall(x, y)
                continue
            if e == 0:
                break
            e -= 1
            x, y = nx[(x, y, s)]
        else:
            c = x * y
            dn = []
            for s in ids:
                if (x, y, s) in nx:
                    dn.append((s, nx[(x, y, s)]))

            if e <= c:
                if not dn:
                    x, y = fall(x, y)
                    continue
                break

            e -= c
            if not dn:
                x, y = fall(x, y)
                continue

            bx, by = 0, -1
            for _, (xx, yy) in dn:
                if yy > by:
                    bx, by = xx, yy

            if e == 0:
                break
            e -= 1
            x, y = bx, by

    print(x, y,end="")


if __name__ == "__main__":
    main()