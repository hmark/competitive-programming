import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, b):
    cache = {}
    for value in b:
        if not value in cache:
            cache[value] = 0
        cache[value] += 1

    a = []
    for key in cache:
        a.append([key, cache[key]])
    a.sort(key=lambda x: x[0])

    if n == 2:
        print(a[0][0], a[0][0])
    else:
        j = 0
        ans = []
        for i in reversed(range(1, n)):
            ans.append(a[j][0])
            a[j][1] -= i
            if a[j][1] == 0:
                j += 1

        ans.append(a[j - 1][0])

        print(" ".join([str(x) for x in ans]))


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    task(n, b)
