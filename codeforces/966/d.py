import sys
import math
from collections import deque


def task(n, a, s):

    total = sum(a)
    li = 0
    ri = n - 1
    ans = 0

    while True:
        # print(li, ri, total, ans)
        if li >= n or ri < 0:
            break
    
        if s[li] != 'L':
            total -= a[li]
            li += 1
        elif s[ri] != 'R':
            total -= a[ri]
            ri -= 1
        elif li >= ri:
            break
        else:
            ans += total

            total -= a[li]
            total -= a[ri]
            li += 1
            ri -= 1

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    task(n, a, s)

