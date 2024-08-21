import sys
import math
from collections import deque

input = sys.stdin.readline

def tester(a1, b1, a2, b2):
    x = 0
    if a1 > b1:
        x += 1
    elif a1 < b1:
        x -= 1

    if a2 > b2:
        x += 1
    elif a2 < b2:
        x -= 1

    return x > 0


def task(a1, a2, b1, b2):
    ans = 0

    if tester(a1, b1, a2, b2):
        ans += 1

    if tester(a1, b2, a2, b1):
        ans += 1

    if tester(a2, b1, a1, b2):
        ans += 1

    if tester(a2, b2, a1, b1):
        ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    task(a1, a2, b1, b2)
