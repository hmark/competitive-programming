import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    mn = a[0]
    for i in range(1, n):
        mn &= a[i]

    if mn >= 1:
        print(1)
        return

    b = None
    ans = 0
    for i in range(n):
        if b == None:
            b = a[i]
        else:
            b &= a[i]

        if b == mn:
            ans += 1
            b = None

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
