import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a, b):
    ab = []

    for i in range(n):
        ab.append([i, a[i] - 1 + b[i] - 1])

    ab = sorted(ab, key=lambda x: -x[1])

    ans = 0
    for i in range(n):
        j = ab[i][0]

        if i % 2 == 0:
            ans += a[j] - 1
        else:
            ans -= b[j] - 1

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, a, b)
