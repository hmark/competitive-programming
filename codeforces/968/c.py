import sys
import math
import string
from collections import deque


def task(n, s):
    table = {}

    for c in s:
        if not c in table:
            table[c] = 0
        table[c] += 1

    a = []
    for c in table:
        a.append([c, table[c]])

    a.sort(key=lambda x: x[1])
    b = deque(a)

    ans = []
    x = b.pop()
    y = None
    
    while len(b) > 0 or x != None or y != None:
        if x == None and len(b) > 0:
            x = b.pop()

        if x != None:
            ans.append(x[0])
            x[1] -= 1
            if x[1] == 0:
                x = None

        if y == None and len(b) > 0:
            y = b.pop()

        if y != None:
            ans.append(y[0])
            y[1] -= 1
            if y[1] == 0:
                y = None

        # print(ans)


    print("".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
