import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    ans = (sum(a) - max(a) - k + 1) * 2 + k - 1

    print(ans)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
