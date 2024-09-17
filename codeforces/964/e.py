import sys
import math
from collections import deque

input = sys.stdin.readline


def task(l, r):
    ans = 0
    temp = l
    tempans = 0

    while temp > 0:
        tempans += 1
        temp = math.floor(temp / 3)
        ans += 2

    l += 1

    threes = [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441]
    for i in threes:
        # print(i, l, r, tempans, ans)
        if l == i:
            tempans += 1
        if l < i:
            ans += (min(r, i - 1) - l + 1) * tempans
            l = i
            tempans += 1
        if r < i:
            break

    print(ans)


t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    task(l, r)
