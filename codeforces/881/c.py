import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    ans = 0
    while n > 0:
        ans += n
        n = n // 2
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
