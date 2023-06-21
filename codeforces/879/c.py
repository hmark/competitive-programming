import sys
import math
from collections import deque


def task(n, s, t):
    trev = t[::-1]
    diff1 = 0
    diff2 = 0

    for i in range(n):
        if s[i] != t[i]:
            diff1 += 1
        if s[i] != trev[i]:
            diff2 += 1

    ans1 = 2 * diff1
    if diff1 % 2 == 1:
        ans1 -= 1

    ans2 = 2 * diff2
    if diff2 % 2 == 0:
        ans2 -= 1

    if ans2 < 0:
        ans2 = 2

    ans = min(ans1, ans2)

    # print(s, t, ans1, ans2)
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    tt = input()
    task(n, s, tt)
