import sys
import math
from collections import deque

input = sys.stdin.readline


def task(m, x, c, h):
    hsum = sum(h)
    dp = [0]

    for k in range(hsum):
        dp.append(float('Inf'))

    for i in range(m):
        for k in reversed(range(hsum + 1)):
            prev = k - h[i]
            if prev >= 0 and dp[prev] != float('Inf'):
                # print(k, dp[prev], c[i], i, i * x)
                if dp[prev] + c[i] <= i * x:
                    dp[k] = min(dp[k], dp[prev] + c[i])
        # print(c[i], h[i], dp)

    for k in reversed(range(hsum + 1)):
        if dp[k] != float('Inf'):
            print(k)
            return


t = int(input())
for _ in range(t):
    m, x = map(int, input().split())
    c = []
    h = []
    for i in range(m):
        cc, hh = map(int, input().split())
        c.append(cc)
        h.append(hh)
    task(m, x, c, h)
