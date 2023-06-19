import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    cache = []
    for i in range(101):
        cache.append(0)

    for i in a:
        cache[i] += 1

    curr = cache[0]
    for i in range(1, 101):
        if cache[i] > curr:
            print("NO")
            return
        else:
            curr = cache[i]

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
