import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, x, y):
    ver = []
    hor = []
    fall = []
    rise = []

    for i in range(n):
        hor.append(x[i])
        ver.append(y[i])
        fall.append(x[i] + y[i])
        rise.append(x[i] - y[i])

    arrs = [ver, hor, fall, rise]
    ans = 0

    for arr in arrs:
        c = dict()

        for value in arr:
            if not value in c:
                c[value] = 0
            c[value] += 1

        for value in c:
            if c[value] > 1:
                ans += c[value] * (c[value] - 1)

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xx, yy = map(int, input().split())
        x.append(xx)
        y.append(yy)
    task(n, x, y)
