import sys
import math
from collections import deque
from functools import cmp_to_key

input = sys.stdin.readline


def compare(x, y):
    l = x[1] * y[2]
    r = x[2] * y[1]
    if l > r:
        return -1
    elif l < r:
        return 1
    elif x[0] < y[0]:
        return -1
    else:
        return 1


def task(n, ab):
    # ab.sort(key=lambda x: (x[3], x[4]), reverse=True)
    ab.sort(key=cmp_to_key(compare))
    ab = [str(x[0]) for x in ab]
    print(" ".join(ab))


n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    rate = a / (a + b)
    ab.append([i + 1, a, b, rate, n - i])
task(n, ab)
