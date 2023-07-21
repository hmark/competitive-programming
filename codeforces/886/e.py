import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, c, s):
    for i in range(n):
        c -= s[i] ** 2

    l = -1
    r = 10000000000000000000
    a = sum(s)
    # print(c)
    while l + 1 < r:
        j = l + (r - l) // 2

        k = 4 * n * (j ** 2) + 4 * a * j
        # print(l, r, j, k, c, a)
        if k == c:
            print(j)
            return
        elif k > c:
            r = j
        else:
            l = j

    print(j)


t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))
    task(n, c, s)
