import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    ans = []
    ans.append(['1', '1'])
    ans.append([str(n), str(n)])
    ans.append(['1', '2'])
    ans.append([str(n - 1), '1'])

    for i in range(3, n - 1):
        ans.append(['1', str(i)])

    for i in range(n):
        print(" ".join(ans[i]))


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
