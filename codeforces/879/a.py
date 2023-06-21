import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    neg = 0
    for i in a:
        if i < 0:
            neg += 1

    pos = n - neg
    ans = max(0, math.ceil((neg - pos) / 2))
    neg -= ans

    if neg % 2 != 0:
        ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
