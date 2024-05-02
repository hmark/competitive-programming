import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, x):
    mn = max(x)
    ans = [mn + 1]
    for i in range(n - 1):
        ans.append(ans[-1] + x[i])
    print(" ".join([str(aa) for aa in ans]))


t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    task(n, x)
