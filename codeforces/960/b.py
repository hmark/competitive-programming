import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, x, y):
    ans = []
    for i in range(1, n + 1):
        if y <= i and i <= x:
            ans.append("1")
        elif x < i and (i - x) % 2 == 0:
            ans.append("1")
        elif i < y and (y - i) % 2 == 0:
            ans.append("1")
        else:
            ans.append("-1")

    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    task(n, x, y)
