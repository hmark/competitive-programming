import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    table = []
    for i in range(n + 2):
        table.append(False)

    for i in range(n):
        if i != 0:
            if table[a[i] - 1] == False and table[a[i] + 1] == False:
                print("NO")
                return

        table[a[i]] = True

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
