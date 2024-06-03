import sys
import math
from collections import deque


def task(n, m, s):
    cache = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    for c in s:
        cache[c] += 1

    ans = 0
    for c in cache:
        ans += m - min(cache[c], m)

    # print(cache)
    print(ans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    task(n, m, s)
