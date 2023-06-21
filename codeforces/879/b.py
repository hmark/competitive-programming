import sys
import math
from collections import deque

input = sys.stdin.readline


def task(l, r):
    if len(l) < len(r):
        l = "0" * (len(r) - len(l)) + l

    ans = 0
    flag = False
    for i in range(len(l)):
        a = int(l[i])
        b = int(r[i])

        if not flag:
            if a == b:
                continue
            else:
                ans += b - a
                flag = True
        else:
            ans += 9

    print(ans)


t = int(input())
for _ in range(t):
    l, r = map(str, input().split())
    task(l, r)
