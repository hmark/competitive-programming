import sys
import math
from collections import deque


def task(n, m, s):
    ss = ["v", "i", "k", "a"]
    nxt = ss.pop(0)

    for i in range(m):
        for j in range(n):
            # print(i, j, s[j][i], nxt)
            if s[j][i] == nxt:
                if len(ss) == 0:
                    print("YES")
                    return
                else:
                    nxt = ss.pop(0)
                break

    print("NO")


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    task(n, m, s)
