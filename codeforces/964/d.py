import sys
import math
from collections import deque


def task(s, u):
    ans = []
    si = 0
    ui = 0

    while si < len(s):
        if s[si] == "?":
            if ui < len(u):
                ans.append(u[ui])
                si += 1
                ui += 1
            else:
                ans.append('a')
                si += 1
        elif ui >= len(u):
            ans.append(s[si])
            si += 1
        elif s[si] == u[ui]:
            ans.append(s[si])
            si += 1
            ui += 1
        else:
            ans.append(s[si])
            si += 1

    if ui < len(u):
        print("NO")
    else:
        print("YES")
        print("".join(ans))


t = int(input())
for _ in range(t):
    s = input()
    u = input()
    task(s, u)
