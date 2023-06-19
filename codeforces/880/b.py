import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, g):
    if n <= 2:
        print(0)
        return

    total = k * g
    d = math.floor((g - 1) / 2)
    ans = min(total, (n - 1) * d)
    remaining = (total - ans) % g

    if remaining <= d:
        ans += remaining
    else:
        ans -= g - remaining

    print(max(ans, 0))


t = int(input())
for _ in range(t):
    n, k, g = map(int, input().split())
    task(n, k, g)
