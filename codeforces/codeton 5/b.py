import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, x, a, b, c):
    temp = 0
    for aa in a:
        if aa & x == aa:
            temp |= aa
        else:
            break

    for bb in b:
        if bb & x == bb:
            temp |= bb
        else:
            break

    for cc in c:
        if cc & x == cc:
            temp |= cc
        else:
            break

    if temp == x:
        print("Yes")
    else:
        print("No")


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    task(n, x, a, b, c)
