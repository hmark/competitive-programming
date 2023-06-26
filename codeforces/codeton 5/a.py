import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, a, b):
    a.sort()
    b.sort()

    while len(a) > 0 and len(b) > 0:
        diff = min(a[len(a) - 1], b[len(b) - 1])
        a[len(a) - 1] -= diff
        b[len(b) - 1] -= diff

        if a[len(a) - 1] <= 0:
            a.pop()

        if b[len(b) - 1] <= 0:
            b.pop()

    if len(a) > 0:
        print("Tsondu")
    elif len(b) > 0:
        print("Tenzing")
    else:
        print("Draw")


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, m, a, b)
