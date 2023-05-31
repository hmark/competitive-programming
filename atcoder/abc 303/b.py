import math


def task(n, m, a):
    cache = {}

    for i in range(n):
        cache[i + 1] = set()

    for i in range(m):
        for j in range(n - 1):
            cache[a[i][j]].add(a[i][j + 1])
            cache[a[i][j + 1]].add(a[i][j])

    ans = 0
    for i in range(n):
        ans += n - 1 - len(cache[i + 1])
    ans = math.floor(ans / 2)
    print(ans)


n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
task(n, m, a)
