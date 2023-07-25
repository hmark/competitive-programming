import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, c):
    a = c[0]
    b = c[-1]
    ka = k
    kb = k

    if a == b:
        ka = 0

    for x in c:
        if ka > 0:
            if x == a:
                ka -= 1
        elif kb > 0:
            if x == b:
                kb -= 1
        if ka == 0 and kb == 0:
            print("YES")
            return

    print("NO")


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    task(n, k, c)
