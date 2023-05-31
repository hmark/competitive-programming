def task(n, m, h, k, s, xs, ys):
    cache = {}
    for i in range(m):
        if not xs[i] in cache:
            cache[xs[i]] = set()
        cache[xs[i]].add(ys[i])

    x = 0
    y = 0
    for c in s:
        if c == "R":
            x += 1
        elif c == "L":
            x -= 1
        elif c == "U":
            y += 1
        elif c == "D":
            y -= 1
        h -= 1
        if h < 0:
            print("No")
            return
        elif h < k and x in cache and y in cache[x]:
            h = k
            cache[x].remove(y)
    print("Yes")


n, m, h, k = map(int, input().split())
s = input()
x = []
y = []
for i in range(m):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
task(n, m, h, k, s, x, y)
