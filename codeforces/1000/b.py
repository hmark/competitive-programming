import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, l, r, a):
    left = sorted(a[:l-1])
    mid = list(reversed(sorted(a[l-1:r])))
    right = sorted(a[r:])
    # print(left, mid, right)

    diff_left = 0
    diff_right = 0

    i = 0
    for i in range(len(left)):
        if i < len(mid):
            if mid[i] > left[i]:
                diff_left += mid[i] - left[i]
        else:
            break

    i = 0
    for i in range(len(right)):
        if i < len(mid):
            if mid[i] > right[i]:
                diff_right += mid[i] - right[i]
        else:
            break

    ans = sum(mid) - max(diff_left, diff_right)
    print(ans)


t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, l, r, a)
