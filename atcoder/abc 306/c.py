import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    cache = []
    for i in range(n + 1):
        cache.append([0, 0, 0])

    for i in range(3*n):
        cache[a[i]][2] = a[i]
        cache[a[i]][1] += 1
        if cache[a[i]][1] == 2:
            cache[a[i]][0] = i + 1
    cache = sorted(cache, key=lambda x: x[0])

    ans = []
    for i in range(1, n + 1):
        ans.append(str(cache[i][2]))
    print(" ".join(ans))


n = int(input())
a = list(map(int, input().split()))
task(n, a)
