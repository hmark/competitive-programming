import sys
import math
from collections import deque


def task(s1, s2, t, q, qs):
    s1 = list(" " + s1)
    s2 = list(" " + s2)
    ss = [[], s1, s2]

    diffs = set()
    unblocks = {}
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs.add(i)

    for i in range(q):
        if i in unblocks:
            diffs.add(unblocks[i])

        length = len(qs[i])
        if length == 1:
            if len(diffs) > 0:
                print("NO")
            else:
                print("YES")
        elif length == 2:
            _, pos = qs[i]
            if pos in diffs:
                diffs.remove(pos)
                ft = i + t
                unblocks[ft] = pos
        elif length == 5:
            _, ss1, pos1, ss2, pos2 = qs[i]
            temp = ss[ss1][pos1]
            ss[ss1][pos1] = ss[ss2][pos2]
            ss[ss2][pos2] = temp

            if pos1 in diffs:
                diffs.remove(pos1)

            if pos2 in diffs:
                diffs.remove(pos2)

            if s1[pos1] != s2[pos1]:
                diffs.add(pos1)

            if s1[pos2] != s2[pos2]:
                diffs.add(pos2)


t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    t, q = map(int, input().split())
    qs = []
    for __ in range(q):
        qs.append(list(map(int, input().split())))
    task(s1, s2, t, q, qs)
