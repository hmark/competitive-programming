import sys
import math
from collections import deque

input = sys.stdin.readline


def task(s):
    val = 0
    last = None
    
    for c in s:
        if c != last:
            last = c
            val = 1
        else:
            val += 1
            if val == 7:
                print("YES")
                return

    print("NO")


s = input()
task(s)
