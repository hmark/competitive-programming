import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    ans = 0
    evens = 0
    for aa in a:
        if aa % 2 == 0:
            evens += 1

    odds = n - evens
    ans = 0

    if evens > 0:
        ans = 1 + odds
    elif odds > 1:
        ans = odds - 1 

    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
