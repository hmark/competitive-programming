import sys
import math
from collections import deque


def task(s):
    a = list(map(int, s.split('+')))
    a.sort()
    print("+".join([str(val) for val in a]))


s = input()
task(s)
