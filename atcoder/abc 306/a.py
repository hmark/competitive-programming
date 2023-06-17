import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, s):
    ans = []
    for c in s:
        ans.append(c)
        ans.append(c)
    print("".join(ans))


n = int(input())
s = input()
task(n, s)
