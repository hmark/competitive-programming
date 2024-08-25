
import sys
import math
from collections import deque


def task(n, s):
    if s[0] == s[-1]:
        print("NO")
    else:
        print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
