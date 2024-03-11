import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    for i in range(n - 2):
        if a[i] < 0:
            print("NO")
            return
        x = a[i]
        a[i] = 0
        a[i + 1] -= x * 2
        a[i + 2] -= x

    if a[-1] == 0 and a[-2] == 0 and a[-3] == 0:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
