import sys
import math
from collections import deque

input = sys.stdin.readline


def task(l, r):
    if r == 1:
        print(1)
    else:
        print(r - l)


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    task(l, r)
