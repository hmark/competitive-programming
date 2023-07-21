import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    a.sort()
    best = 1
    current = 1
    # print(a)
    for i in range(1, n):
        if a[i] - a[i - 1] <= k:
            current += 1
        else:
            # print(i, current, best)
            best = max(best, current)
            current = 1
    best = max(best, current)

    print(n - best)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
