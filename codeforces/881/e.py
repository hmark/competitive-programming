import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, lr, q, xs):
    l = -1
    r = q + 1

    while r - l > 1:
        mm = (r + l) // 2

        # print(l, r, m)

        cache = [0] * (n + 1)

        for i in range(mm):
            cache[xs[i]] = 1

        for i in range(1, n + 1):
            cache[i] += cache[i - 1]

        found = False
        for i in range(m):
            ss, se = lr[i]
            if se - ss + 1 < (cache[se] - cache[ss - 1]) * 2:
                found = True
                break

        if found:
            r = mm
        else:
            l = mm

        # print(cache, found, i)

    if r > q:
        print(-1)
    else:
        print(r)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lr = []
    for i in range(m):
        l, r = map(int, input().split())
        lr.append([l, r])
    q = int(input())
    xs = []
    for i in range(q):
        x = int(input())
        xs.append(x)
    task(n, m, lr, q, xs)
