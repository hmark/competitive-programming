import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, ls):
    mx = 0
    for a in ls:
        table = {}

        for i in range(len(a)):
            if not a[i] in table:
                table[a[i]] = True

        found1 = False
        for i in range(500000):
            if not i in table:
                if found1 == False:
                    found1 = True
                else:
                    mx = max(mx, i)
                    break

    ans = (min(mx, m) + 1) * mx
    if mx < m:
        ans += (m + 1) * m // 2 - (mx + 1) * mx // 2
    print(ans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ls = []
    for i in range(n):
        ls.append(list(map(int, input().split()[1:])))
    task(n, m, ls)
