import sys
import math
from collections import deque


def task(a, b):
    ans = len(a) + len(b)
    for i in range(len(b)):
        next = i
        suma = i + len(a)

        for j in range(len(a)):
            if a[j] == b[next]:
                next += 1
                if next == len(b):
                    break
        
        suma += len(b) - next
        ans = min(ans, suma)

    print(ans)


t = int(input())
for _ in range(t):
    a = input()
    b = input()
    task(a, b)
