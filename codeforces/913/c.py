import sys
import math
from collections import deque


def task(n, s):
    cache = {}

    for c in s:
        if not c in cache:
            cache[c] = 0
        cache[c] += 1

    mx = 0
    for c in cache:
        mx = max(mx, cache[c])

    # print(cache, mx)
    diff = n - mx

    if mx >= diff:
        print(mx - diff)
    elif n % 2 == 0:
        print(0)
    else:
        print(1)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
