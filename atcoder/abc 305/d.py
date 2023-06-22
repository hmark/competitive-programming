import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a, q, lr):
    times = set()
    for i in range(q):
        times.add(lr[i][0])
        times.add(lr[i][1])

    b = list(times)
    b.sort()
    b = deque(b)

    cache = {}
    total = 0
    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                total += a[i]
            else:
                total += a[i] - a[i - 1]
        while len(b) > 0 and b[0] <= a[i]:
            t = b.popleft()
            if i % 2 == 0:
                cache[t] = total - (a[i] - t)
            else:
                cache[t] = total

    for i in range(q):
        print(cache[lr[i][1]] - cache[lr[i][0]])


n = int(input())
a = list(map(int, input().split()))
q = int(input())
lr = []
for i in range(q):
    lr.append(list(map(int, input().split())))
task(n, a, q, lr)
