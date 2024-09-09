import sys
import math
from collections import deque


def task(n, a1, a2):
    regions = 0
    empties = []

    start = False
    for i in range(n):
        empty = 0
        if a1[i] == '.':
            empty += 1
        if a2[i] == '.':
            empty += 1
        empties.append(empty)
        
        if start:
            if a1[i] == '.' and a2[i] == '.':
                continue

            if (a1[i - 1] == 'x' or a1[i] == 'x') and (a2[i - 1] == 'x' or a2[i] == 'x'):
                start = False
        
        if not start and (a1[i] == '.' or a2[i] == '.'):
            regions += 1
            start = True
    # print('reg', regions)

    if regions >= 3 or regions == 0:
        print(0)
    elif regions == 1:
        ans = 0
        for i in range(2, n - 2):
            if empties[i - 1] == 1 and empties[i] == 2 and empties[i + 1] == 1 and ((a1[i - 1] == '.' and a1[i + 1] == '.') or (a2[i - 1] == '.' and a2[i + 1] == '.')):
                ans += 1
        print(ans)
    elif regions == 2:
        ans = 0
        for i in range(1, n - 1):
            neighbors = 0
            if a1[i] == '.':
                if a1[i - 1] == '.':
                    neighbors += 1
                if a1[i + 1] == '.':
                    neighbors += 1
                if a2[i] == '.':
                    neighbors += 1
                if neighbors == 2:
                    ans += 1
            neighbors = 0
            if a2[i] == '.':
                if a2[i - 1] == '.':
                    neighbors += 1
                if a2[i + 1] == '.':
                    neighbors += 1
                if a1[i] == '.':
                    neighbors += 1
                if neighbors == 2:
                    ans += 1
        print(ans)
        

    # print(n, a1, a2)


t = int(input())
for _ in range(t):
    n = int(input())
    a1 = 'x' + input() + 'x'
    a2 = 'x' + input() + 'x'
    task(n + 2, a1, a2)
