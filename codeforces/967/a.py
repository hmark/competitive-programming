import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    table = {}
    for aa in a:
        if not aa in table:
            table[aa] = 0
        table[aa] += 1
    
    mx = 0
    for key in table:
        mx = max(mx, table[key])
    
    print(n - mx)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
