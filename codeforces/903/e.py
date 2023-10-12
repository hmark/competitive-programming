import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    cache = [0] * n
    for i in range(n):
        index = n - 1 - i
        if a[index] > i:
            cache[index] = i + 1
        else:
            cache[index] = i - a[index]
            if index + a[index] + 1 < n:
                cache[index] = min(
                    cache[index], cache[index + a[index] + 1])
        if index + 1 < n:
            cache[index] = min(
                cache[index], cache[index + 1] + 1)

        # print(i, index, a[index], cache)

    print(cache[0])


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
