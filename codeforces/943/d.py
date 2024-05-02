import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, pb, ps, p, a):
    mn = min(n, k)

    currb = 0
    currs = 0
    bestb = 0
    bests = 0

    for i in range(mn):
        b = a[pb - 1] * (k - i) + currb
        s = a[ps - 1] * (k - i) + currs

        if b > bestb:
            bestb = b

        if s > bests:
            bests = s

        currb += a[pb - 1]
        currs += a[ps - 1]

        pb = p[pb - 1]
        ps = p[ps - 1]

    if bestb > bests:
        print("Bodya")
    elif bestb < bests:
        print("Sasha")
    else:
        print("Draw")


t = int(input())
for _ in range(t):
    n, k, pb, ps = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    task(n, k, pb, ps, p, a)
