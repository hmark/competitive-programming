import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    table = []
    for i in range(n + 1):
        table.append(0)

    for aa in a:
        table[aa] += 1

    for aa in reversed(table):
        if aa % 2 == 1:
            print("YES")
            return
        
    print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
