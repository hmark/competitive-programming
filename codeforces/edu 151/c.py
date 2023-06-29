import sys
import math
from collections import deque


def task(s, m, l, r):

    k = 0
    for i in range(m):
        a = set()
        for j in range(int(l[i]), int(r[i]) + 1):
            a.add(j)
        found = True
        while k < len(s):
            c = int(s[k])
            # print(a, c)
            if c in a:
                a.remove(c)
            k += 1
            if len(a) == 0:
                found = False
                break

        if found:
            print("YES")
            return

    print("NO")


t = int(input())
for _ in range(t):
    s = input()
    m = int(input())
    l = input()
    r = input()
    task(s, m, l, r)
