import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    x = math.ceil(math.sqrt(2 * n))
    if x * (x - 1) / 2 > n:
        x -= 1
    ans = x + n - (x * (x - 1) >> 1)
    print(int(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
