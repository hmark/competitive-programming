import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, a):
    arr = []
    for i in range(n):
        arr.append([i + 1, a[i] % k, a[i] % k == 0])
    arr.sort(key=lambda x: (-x[2], -x[1], x[0]))
    # print(arr)
    ans = [str(arr[i][0]) for i in range(n)]
    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
