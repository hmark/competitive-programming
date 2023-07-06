import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    b = []
    for i in range(1, n):
        b.append(abs(a[i - 1] - a[i]))
    b.sort()
    print(sum(b[0:n-k]))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
