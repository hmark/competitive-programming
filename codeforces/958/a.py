import sys
import math
from collections import deque


def task(n, s):
    ones = 0
    zeros = 0
    last = None
    for i in range(n):
        if s[i] == '1':
            ones += 1
        elif last != '0':
            zeros += 1

        last = s[i]

    if ones > zeros:
        print("Yes")
    else:
        print("No")


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
