import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    for i in range(1, n + 1):
        distance = max(n - i, i - 1) * 2
        # print(i, distance, a[i - 1])
        if a[i - 1] <= distance:
            print("NO")
            return
    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
