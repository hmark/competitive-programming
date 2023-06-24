import sys
import math
from collections import deque


def task(n, s):
    brackets = []
    segs = []

    for i in range(n):
        if s[i] == '(':
            brackets.append(i)
        if s[i] == ')' and len(brackets) > 0:
            start = brackets.pop()
            end = i
            segs.append([start, end])

    segs.sort()

    ans = []
    j = 0
    for i in range(n):
        while j < len(segs) and i > segs[j][1]:
            j += 1

        if j < len(segs) and segs[j][0] <= i and i <= segs[j][1]:
            continue

        ans.append(s[i])

    print("".join(ans))


n = int(input())
s = input()
task(n, s)
