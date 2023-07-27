import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    a = [[i + 1, a[i]] for i in range(n)]
    a.sort(key=lambda x: x[1])

    ansi = None
    ansj = None
    ansx = None
    best = -1
    kmin = 0
    kmax = (2 ** k) - 1

    for i in range(1, n):
        bi = a[i - 1][0]
        b = a[i - 1][1]

        ci = a[i][0]
        c = a[i][1]

        d = b & c
        xmax = kmax ^ d
        xmin = kmin ^ d

        mx = (b ^ xmax) & (c ^ xmax)
        mn = (b ^ xmin) & (c ^ xmin)

        if mx > best:
            best = mx
            ansi = bi
            ansj = ci
            ansx = xmax
        elif mn > best:
            best = mn
            ansi = bi
            ansj = ci
            ansx = xmin

    print(ansi, ansj, ansx)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    task(n, k, a)
