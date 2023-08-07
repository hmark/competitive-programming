import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    odds = 0
    evens = 0
    for value in a:
        if value % 2 == 1:
            odds += 1
        else:
            evens += 1

    if odds == 0:
        print("YES")
    elif odds % 2 == 0:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
