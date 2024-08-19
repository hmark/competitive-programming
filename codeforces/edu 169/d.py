import sys
import math
from collections import deque


def task(n, q, a, qs):
    ltable = {"R" : [], "G" : [], "B" : [], "Y" : []}
    rtable = {"R" : [], "G" : [], "B" : [], "Y" : []}

    temps = {"R" : -1, "G" : -1, "B" : -1, "Y" : -1}
    for i in range(n):
        c1 = a[i][0]
        c2 = a[i][1]

        for key in ltable:
            if c1 == key:
                temps[c1] = 0
            elif c2 == key:
                temps[c2] = 0
            elif temps[key] != -1:
                temps[key] += 1

        for key in temps:    
            ltable[key].append(temps[key])

    temps = {"R" : -1, "G" : -1, "B" : -1, "Y" : -1}
    for i in reversed(range(n)):
        c1 = a[i][0]
        c2 = a[i][1]

        for key in rtable:
            if c1 == key:
                temps[c1] = 0
            elif c2 == key:
                temps[c2] = 0
            elif temps[key] != -1:
                temps[key] += 1

        for key in temps:    
            rtable[key].append(temps[key])

    for qq in qs:
        ans = 0
        x = min(qq) - 1
        y = max(qq) - 1

        if x == y:
            ans = 0
        elif a[x][0] == a[y][0] or a[x][0] == a[y][1] or a[x][1] == a[y][0] or a[x][1] == a[y][1]:
            ans = y - x
        else:
            print(ltable)
            print(rtable)
            lans = rans = n

            for key in ltable:
                if ltable[key][y] != -1:
                    lans = min(lans, ltable[key][x])

            for key in rtable:
                if rtable[key][y] != -1:
                    rans = min(lans, rtable[key][x])

            ans = min(lans, rans)

            if ans == n:
                ans = -1
        
        print(ans)


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(input().split())
    qs = []
    for i in range(q):
        qs.append(list(map(int, input().split())))
    task(n, q, a, qs)
