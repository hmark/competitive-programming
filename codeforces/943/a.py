import sys
import math
from collections import deque

input = sys.stdin.readline


def task(x):
    divisors = []
    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)

    mx = 0
    best = 0
    for i in range(x):
        for div in divisors:
            if i % div == 0 and div + i > mx:
                mx = div + i
                best = i
    print(best)


t = int(input())
for _ in range(t):
    x = int(input())
    task(x)
