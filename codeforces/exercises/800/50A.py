import sys
import math
from collections import deque

input = sys.stdin.readline


def task(m, n):
    ans = m * n
    if ans % 2 == 1:
        ans -= 1
    print(ans // 2)


m, n = map(int, input().split())
task(m, n)
