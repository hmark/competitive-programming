import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    if n % 2 == 0:
        print(-1)
    else:
        ans = []
        for i in range(1, n + 1, 2):
            ans.append(str(i))
        for i in reversed(range(2, n, 2)):
            ans.append(str(i))
        print(" ".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
