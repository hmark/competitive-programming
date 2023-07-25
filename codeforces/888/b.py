import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    odds = []
    evens = []

    for x in a:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)

    odds.sort()
    evens.sort()

    odds = deque(odds)
    evens = deque(evens)

    for x in a:
        if len(odds) == 0 or len(evens) == 0:
            break

        if x % 2 == 0:
            if evens[0] > odds[0]:
                print("NO")
                return
            evens.popleft()
        else:
            if evens[0] < odds[0]:
                print("NO")
                return
            odds.popleft()

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
