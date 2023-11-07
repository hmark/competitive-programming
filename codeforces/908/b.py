import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    counts = [0] * 101

    for aa in a:
        counts[aa] += 1

    ans1 = -1
    ans2 = -1
    for i in range(101):
        count = counts[i]

        if count >= 2:
            if ans1 == -1:
                ans1 = i
            elif ans2 == -1:
                ans2 = i
            else:
                break

    # print(counts)
    if ans2 == -1:
        print(-1)
        return

    b = []
    ans1next = 1
    ans2next = 2
    for aa in a:
        if aa == ans1:
            b.append(ans1next)
            if ans1next == 1:
                ans1next = 2
        elif aa == ans2:
            b.append(ans2next)
            if ans2next == 2:
                ans2next = 3
        else:
            b.append(1)
    print(" ".join([str(bb) for bb in b]))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
