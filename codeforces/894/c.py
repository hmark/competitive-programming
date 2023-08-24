import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    b = []

    for i in range(n):
        if i + 1 < n:
            nxt = a[i + 1]
        else:
            nxt = 0

        diff = a[i] - nxt

        if (len(b) + diff) > n:
            print("NO")
            return

        for _ in range(diff):
            b.append(i + 1)

    b = list(reversed(b))

    for i in range(n):
        if a[i] != b[i]:
            print("NO")
            return

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
