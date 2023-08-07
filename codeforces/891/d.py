import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a, b):

    c = []

    for i in range(n):
        c.append([i + 1, a[i] - b[i]])

    c.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    mx = c[0][1]
    ans = []

    for i in range(n):
        if c[i][1] == mx:
            ans.append(str(c[i][0]))
        else:
            break

    print(len(ans))
    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, a, b)
