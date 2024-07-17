import sys
import math
from collections import deque

def task(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            print(-1)
            return
        elif s1[i] > s2[i]:
            print(1)
            return
        
    print(0)


s1 = input().lower()
s2 = input().lower()

task(s1, s2)
