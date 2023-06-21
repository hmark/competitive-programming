import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n):
    if n == 2 or n == 3 or n == 4:
        print("Bob")
    else:
        print("Alice")


t = int(input())
for _ in range(t):
    n = int(input())
    task(n)
