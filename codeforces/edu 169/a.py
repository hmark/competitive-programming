import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    if n == 2 and a[1] - a[0] > 1:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
