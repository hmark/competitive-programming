import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    a.sort()
    ans = 0
    while len(a) > 1:
        ans += a.pop() - a.pop(0)
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
