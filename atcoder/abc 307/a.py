import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    weeks = []

    for i in range(n):
        week = 0
        for j in range(i * 7, min((i + 1) * 7, len(a))):
            week += a[j]
        weeks.append(str(week))

    print(" ".join(weeks))


n = int(input())
a = list(map(int, input().split()))
task(n, a)
