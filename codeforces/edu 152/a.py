import sys
import math
from collections import deque

input = sys.stdin.readline


def task(b, c, h):
    breads = min(b, c + h + 1)
    print(breads * 2 - 1)


t = int(input())
for _ in range(t):
    b, c, h = map(int, input().split())
    task(b, c, h)
