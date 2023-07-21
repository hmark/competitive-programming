import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a):
    a.sort()
    if a[2] + a[1] >= 10:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    task([a, b, c])
