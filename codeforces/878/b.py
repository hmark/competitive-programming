import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k):
    k = min(30, k)
    print(min(n + 1, int(math.pow(2, k))))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    task(n, k)
