import sys
import math
from collections import deque

input = sys.stdin.readline

dp = []
total = 0
for i in range(0, 200005):
    total += i
    dp.append(total)
# print(dp)


def task(n, k, x):
    mins = dp[k]
    maxs = dp[n] - dp[n - k]
    # print(n, k, x, mins, maxs)
    if mins <= x and x <= maxs:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    task(n, k, x)
