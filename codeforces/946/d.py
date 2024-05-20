import sys
import math
from collections import deque


def task(n, ss):
    n = 0
    s = 0
    e = 0
    w = 0

    for c in ss:
        if c == 'W':
            w += 1
        elif c == 'E':
            e += 1
        elif c == 'N':
            n += 1
        elif c == 'S':
            s += 1

    x = max(w - e, e - w)
    y = max(n - s, s - n)

    if x % 2 != 0 or y % 2 != 0:
        print("NO")
        return

    if x == 0 and y == 0 and len(ss) == 2:
        print("NO")
        return

    ans = []
    xx = 0
    yy = 0

    xnxt1 = 'R'
    xnxt2 = 'H'
    ynxt1 = 'H'
    ynxt2 = 'R'

    for c in ss:
        if c == 'W':
            if xx <= 0:
                ans.append(xnxt1)
                xx += 1
            else:
                ans.append(xnxt2)
                xx -= 1

            if xx == 0:
                xnxt1, xnxt2 = xnxt2, xnxt1
        elif c == 'E':
            if xx >= 0:
                ans.append(xnxt1)
                xx -= 1
            else:
                ans.append(xnxt2)
                xx += 1

            if xx == 0:
                xnxt1, xnxt2 = xnxt2, xnxt1
        elif c == 'N':
            if yy <= 0:
                ans.append(ynxt1)
                yy += 1
            else:
                ans.append(ynxt2)
                yy -= 1

            if yy == 0:
                ynxt1, ynxt2 = ynxt2, ynxt1
        elif c == 'S':
            if yy >= 0:
                ans.append(ynxt1)
                yy -= 1
            else:
                ans.append(ynxt2)
                yy += 1

            if yy == 0:
                ynxt1, ynxt2 = ynxt2, ynxt1

    # print(xx, yy, ans)
    if xx != 0 or yy != 0:
        print("NO")
        return

    print("".join(ans))


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
