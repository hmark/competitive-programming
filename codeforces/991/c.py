import sys
import math
from collections import deque

# input = sys.stdin.readline

def task(s):
    twos = 0
    threes = 0
    for c in s:
        if c == '2':
            twos += 1
        elif c == '3':
            threes += 1

    digits = []
    for digit in s:
        digits.append(int(digit))   
    diff = sum(digits) % 9

    if diff == 0:
        print("YES")
        return
    else:
        for i in range(min(10, threes + 1)):
            for j in range(min(10, twos + 1)):
                if (diff + i * 6 + j * 2) % 9 == 0:
                    print("YES")
                    return

    print("NO")
    return


t = int(input())
for _ in range(t):
    s = input()
    task(s)
