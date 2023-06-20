import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    ans = 0
    t = 0
    flag = False
    for i in a:
        if flag and i > 0:
            flag = False

        if not flag and i < 0:
            t += 1
            flag = True

        ans += abs(i)
    print(ans, t)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
