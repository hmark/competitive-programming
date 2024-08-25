import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    a.sort()
    if n % 2 == 0:
        print(a[n // 2])
    else:
        print(a[(n - 1) // 2])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
