# Dynamic Programming
# Combinatorics

import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m):
    row1 = [0] * (n + 1)
    row2 = [0] * (n + 1)
    dp = [row1, row2]

    dp[1][1] = m

    for i in range(1, n):
        dp[0][i + 1] = (dp[0][i] * (m - 2)) + (dp[1][i] * (m - 1))
        dp[1][i + 1] = dp[0][i]

        dp[0][i + 1] %= 998244353
        dp[1][i + 1] %= 998244353

    print(dp[0][n])


n, m = map(int, input().split())
task(n, m)
