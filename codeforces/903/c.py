import sys
import math
from collections import deque


def task(n, a):
    half = n // 2
    ans = 0

    for i in range(half):
        for j in range(half):
            val1 = ord(a[i][j])
            val2 = ord(a[j][n - 1 - i])
            val3 = ord(a[n - 1 - i][n - 1 - j])
            val4 = ord(a[n - 1 - j][i])

            mx = max(val1, val2, val3, val4)

            ans += mx - val1
            ans += mx - val2
            ans += mx - val3
            ans += mx - val4
            # print(i, j, val1, val2, val3, val4, ans)

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    task(n, a)
