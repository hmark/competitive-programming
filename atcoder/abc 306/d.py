import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, xy):
    dp0 = 0
    dp1 = 0

    for i in range(n):
        x = xy[i][0]
        y = xy[i][1]

        if x == 0:
            dp0 = max(dp0, dp0 + y, dp1 + y)
        else:
            dp1 = max(dp1, dp0 + y)

    print(max(dp0, dp1))


n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
task(n, xy)
