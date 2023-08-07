import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    print(n, a)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
