import sys
import math
from collections import deque

input = sys.stdin.readline


def task(x):
    ans = x
    a = [int(c) for c in str(x)]
    a.reverse()
    i = 0
    j = 0
    plus = False

    while i < len(a):
        if plus:
            a[i] += 1
            plus = False

        if a[i] >= 5:
            a[i] = 0
            plus = True

            for k in range(j, i):
                a[k] = 0

            j = i

        i += 1
        # print(a, plus)

    if plus:
        a.append(1)

    a.reverse()

    print("".join([str(x) for x in a]))


t = int(input())
for _ in range(t):
    x = int(input())
    task(x)
