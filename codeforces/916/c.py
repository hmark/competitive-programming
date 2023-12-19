import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a, b):
    mxs = []
    mx = 0

    for bb in b:
        mx = max(mx, bb)
        mxs.append(mx)

    best = 0
    suma = 0
    for i in range(min(n, k)):
        aa = a[i]
        bb = b[i]
        mx = mxs[i]
        suma += aa
        best = max(best, suma + mxs[i] * (k - i - 1))

    print(best)


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, k, a, b)
