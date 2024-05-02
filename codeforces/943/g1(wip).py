import sys
import math
from collections import deque


def findall(p, s):
    i = s.find(p)
    while i != -1:
        # print(s, p, i)
        yield i
        i = s.find(p, i + len(p))


def task(n, l, r, s):

    if l == 1:
        print(n)
        return

    ans = 0
    mx = n // l

    for i in range(1, mx + 1):
        ss = s[0:i]
        cnt = 0

        for x in findall(ss, s):
            cnt += 1

        if cnt >= l:
            ans = i
        else:
            break

    print(ans)


t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    s = input()
    task(n, l, r, s)
