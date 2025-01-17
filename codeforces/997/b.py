import sys
import math
from collections import deque

input = sys.stdin.readline

def task(n, g):
    table = {}
    for i in range(n):
        table[i] = []
        for j in range(n):
            if i < j and g[i][j] == '1':
                table[i].append(j)
    
    # print(table)
    empties = []
    ans = []
    for i in range(n):
        empties.append(i)
        ans.append(None)

    for i in range(n):
        right = len(table[i])
        position = empties[len(empties) - right - 1]
        ans[position] = str(i + 1)
        empties.remove(position)

    print(" ".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    g = []
    for i in range(n):
        g.append(input())
    task(n, g)
 