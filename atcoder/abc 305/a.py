import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    diff = n % 5
    if diff > 2:
        print(n + 5 - (n % 5))
    else:
        print(n - n % 5)


n = int(input())
task(n,)
