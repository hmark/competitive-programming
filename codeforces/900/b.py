import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    ans = [2, 3]
    nxt = 3
    for i in range(2, n):
        nxt += 1
        if 3 * nxt % (ans[i - 2] + ans[i - 1]) == 0:
            nxt += 1
        ans.append(nxt)
    print(" ".join([str(x) for x in ans]))


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
