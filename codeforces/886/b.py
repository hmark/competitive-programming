import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a, b):
    ans = -1
    best = -1

    for i in range(n):
        if a[i] <= 10 and b[i] > best:
            ans = i + 1
            best = b[i]
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)
    task(n, a, b)
