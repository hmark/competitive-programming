import sys
import math
from collections import deque


def task(n, m, a, s):
    b = []

    left = 0
    right = n - 1
    for c in s:
        if c == 'L':
            b.append(a[left])
            left += 1
        else:
            b.append(a[right])
            right -= 1

    b.reverse()
    ans = []
    product = 1

    for bb in b:
        product %= m
        bb %= m
        product *= bb
        ans.append(product % m)

    ans.reverse()
    for ansans in ans:
        print(ansans)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    task(n, m, a, s)
