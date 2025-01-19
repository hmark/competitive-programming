import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a):
    b = []
    b.append(a[0] + a[1])
    b.append(a[2] - a[1])
    b.append(a[3] - a[2])
    # print(b)

    if b[0] == b[1] and b[1] == b[2]:
        print(3)
    elif b[0] == b[1] or b[0] == b[2] or b[1] == b[2]:
        print(2)
    else:
        print(1)




t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    task(a)
