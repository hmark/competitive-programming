import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    counts = [0] * (n + 1)
    dp = [0] * (n + 1)

    for i in range(n):
        if a[i] <= n:
            counts[a[i]] += 1
    # print(counts)
    for i in range(n + 1):
        if counts[i] > 0:
            curr = i
            while curr <= n:
                dp[curr] += counts[i]
                curr += i
    # print(dp)
    print(max(dp))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
