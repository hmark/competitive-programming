import sys
import math
from collections import deque

input = sys.stdin.readline


def task(a, b):
    print(a + b)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    task(a, b)
