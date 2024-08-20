import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    table = {}
    
    for i in range(n):
        if not a[i] in table:
            table[a[i]] = []
        table[a[i]] = i

    checks = set()
    for key in table:
        checks.add(table[key])
    # print(checks)

    maxing = True
    ans = []
    mn = None
    mx = None

    for i in range(n):
        if not a[i] in table:
            continue

        if mn == None:
            mn = a[i]
        else:
            mn = min(mn, a[i])

        if mx == None:
            mx = a[i]
        else:
            mx = max(mx, a[i])

        # print(i, a[i], maxing, mn, mx, ans, i in checks)
        if i in checks:
            if maxing:
                ans.append(str(mx))
                del table[mx]
                maxing = False

                if a[i] != mx:
                    ans.append(str(a[i]))
            else:
                ans.append(str(mn))
                del table[mn]
                maxing = True

                if a[i] != mn:
                    ans.append(str(a[i]))

    print(len(ans))
    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
