import sys
import math
from collections import deque


def task(s):
    lowers = []
    uppers = []
    ans = []

    lowersToDelete = 0
    uppersToDelete = 0

    for c in reversed(s):
        if c == 'B':
            uppersToDelete += 1
        elif c == 'b':
            lowersToDelete += 1
        elif c.isupper():
            if uppersToDelete > 0:
                uppersToDelete -= 1
            else:
                ans.append(c)
        else:
            if lowersToDelete > 0:
                lowersToDelete -= 1
            else:
                ans.append(c)

    print("".join(reversed(ans)))


t = int(input())
for _ in range(t):
    s = input()
    task(s)
