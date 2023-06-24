import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a, b, c, k):
    amin = int(math.pow(10, a - 1))
    amax = int(math.pow(10, a))

    bmin = int(math.pow(10, b - 1))
    bmax = int(math.pow(10, b)) - 1

    cmin = int(math.pow(10, c - 1))
    cmax = int(math.pow(10, c)) - 1

    # print(a, b, c, amin, amax, bmin, bmax, cmin, cmax)
    for a in range(amin, amax):

        if cmax < a:
            continue

        b1 = max(bmin, cmin - a)
        b2 = min(bmax, cmax - a)

        d = b2 - b1 + 1

        # print(a, b1, b2, d, k)

        if d <= 0:
            continue

        if k > d:
            k -= d
        else:
            b = b1 + k - 1
            c = a + b
            print(str(a) + " + " + str(b) + " = " + str(c))
            return

    print(-1)


t = int(input())
for _ in range(t):
    a, b, c, k = map(int, input().split())
    task(a, b, c, k)
