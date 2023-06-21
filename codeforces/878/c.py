import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, q, a):
    ans = 0
    seq = 0
    for t in a:
        if t <= q:
            seq += 1
        else:
            seq = 0

        if seq >= k:
            ans += (seq - k + 1)

    print(ans)


t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, q, a)
