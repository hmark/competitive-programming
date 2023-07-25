import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, k, hh, h):
    ans = 0

    for p in h:
        diff = abs(p - hh)
        if diff > 0 and diff % k == 0 and diff // k < m:
            # print(p, diff, k, m)
            ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    n, m, k, hh = map(int, input().split())
    h = list(map(int, input().split()))
    task(n, m, k, hh, h)
