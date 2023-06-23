# Binary Search

import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    a.sort()
    l = 0
    r = a[-1]

    while r - l > 0:
        m = (l + r) // 2
        i = 0
        while i + 1 < len(a) and a[i + 1] - a[0] <= 2 * m:
            i += 1

        j = n - 1
        while j - 1 >= 0 and a[-1] - a[j - 1] <= 2 * m:
            j -= 1

        i += 1
        j -= 1

        if i > j or a[j] - a[i] <= 2 * m:
            r = m
        else:
            if l == m:
                l = r
            else:
                l = m

    print(r)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
