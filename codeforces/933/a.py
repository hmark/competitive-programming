import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, m, k, b, c):
    ans = 0
    for bb in b:
        for cc in c:
            if bb + cc <= k:
                ans += 1
    print(ans)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    task(n, m, k, b, c)
