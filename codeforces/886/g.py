import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, x, y):
    ver = dict()
    hor = dict()
    fall = dict()
    rise = dict()

    for i in range(n):
        hor.setdefault(x[i], 0)
        hor[x[i]] += 1

        ver.setdefault(y[i], 0)
        ver[y[i]] += 1

        fall.setdefault(x[i] + y[i], 0)
        fall[x[i] + y[i]] += 1

        rise.setdefault(x[i] - y[i], 0)
        rise[x[i] - y[i]] += 1

    ans = 0

    for key, value in hor.items():
        ans += value * (value - 1)

    for key, value in ver.items():
        ans += value * (value - 1)

    for key, value in fall.items():
        ans += value * (value - 1)

    for key, value in rise.items():
        ans += value * (value - 1)

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
