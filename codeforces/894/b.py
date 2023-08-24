import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, b):
    a = [str(b[0])]
    for i in range(1, n):
        if b[i] >= b[i - 1]:
            a.append(str(b[i]))
        else:
            a.append(str(b[i]))
            a.append(str(b[i]))
    print(len(a))
    print(" ".join(a))


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    task(n, b)
