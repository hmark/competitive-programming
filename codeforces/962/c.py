import sys
import math
from collections import deque


def task(n, a, b, qs):
    table_a = []
    table_b = []

    ta = []
    tb = []
    for i in range(26):
        ta.append(0)
        tb.append(0)

    table_a.append(ta.copy())
    table_b.append(tb.copy())

    for i in range(n):
        ax = ord(a[i]) - 97
        bx = ord(b[i]) - 97

        ta[ax] += 1
        tb[bx] += 1

        table_a.append(ta.copy())
        table_b.append(tb.copy())

    for q in qs:
        l = q[0]
        r = q[1]
        ans = 0

        for j in range(26):
            a_count = table_a[r][j] - table_a[l - 1][j] 
            b_count = table_b[r][j] - table_b[l - 1][j]

            if a_count > b_count:
                ans += a_count - b_count
        print(ans)


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = input()
    b = input()
    qs = []
    for i in range(q):
        qs.append(list(map(int, input().split())))
    task(n, a, b, qs)
