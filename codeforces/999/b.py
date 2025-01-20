import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, a):
    a.sort()

    leg = None
    for i in reversed(range(1, n)):
        if a[i] == a[i - 1]:
            leg = a[i]
            break

    if leg == None:
        print(-1)
        return
    
    b1 = None
    b2 = None

    legchecks = 2

    for aa in a:
        if aa == leg and legchecks > 0:
            legchecks -= 1
        else:
            if b1 == None:
                b1 = aa
            elif b2 == None:
                b2 = aa

        if b1 != None and b2 != None:
            if b1 + 2 * leg > b2:
                print(leg, leg, b1, b2)
                return
            else:
                b1 = b2
                b2 = None
            
    print(-1)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
