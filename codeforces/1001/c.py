import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    b = a
    ans = sum(b)
    while len(b) > 1:
        c = []
        for i in range(1, len(b)):
            c.append(b[i] - b[i - 1])
        b = c
        ans = max(ans, abs(sum(b)))

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
