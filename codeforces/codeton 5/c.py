# Dynamic Programming

import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    dp = [0] * n
    mins = [math.inf] * (n + 1)
    mins[a[0]] = 0

    for i in range(1, n):
        dp[i] = max(dp[i - 1], i + 1 - mins[a[i]])
        mins[a[i]] = min(mins[a[i]], mins[a[i - 1]] + 1, i - dp[i - 1])

        # print(i, a[i], dp, mins)

    print(dp[n - 1])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
