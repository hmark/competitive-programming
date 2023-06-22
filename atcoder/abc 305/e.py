import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, k, ab, ph):
    g = {}
    cache = [-1]

    for i in range(n):
        g[i + 1] = []
        cache.append(-1)

    for i in range(m):
        g[ab[i][0]].append(ab[i][1])
        g[ab[i][1]].append(ab[i][0])

    ph.sort(key=lambda x: x[1], reverse=True)

    q = deque()
    for i in range(k):
        q.append(ph[i])

        while len(q) > 0:
            phs = q.popleft()
            p = phs[0]
            h = phs[1]

            if cache[p] < h:
                cache[p] = h
                h -= 1

                if h >= 0:
                    for u in g[p]:
                        if cache[u] < h:
                            q.append([u, h])

    ans = []
    for i in range(1, n + 1):
        if cache[i] >= 0:
            ans.append(str(i))

    print(len(ans))
    print(" ".join(ans))


n, m, k = map(int, input().split())
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))
ph = []
for i in range(k):
    ph.append(list(map(int, input().split())))
task(n, m, k, ab, ph)
