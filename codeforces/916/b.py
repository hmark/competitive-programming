import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k):
    ans = []

    for i in reversed(range(1, n - k + 1)):
        ans.append(i)

    for i in range(n - k + 1, n + 1):
        ans.append(i)

    print(" ".join([str(x) for x in ans]))


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    task(n, k)
