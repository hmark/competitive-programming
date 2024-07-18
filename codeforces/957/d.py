import sys
import math
from collections import deque
    
    
def task(n, m, k, a):
    a += 'L'
    pos = -1
    lastpos = None
    in_water = False
    
    while pos != lastpos and pos != n:
        lastpos = pos
    
        if not in_water:
            max_water = None
            jump_to_water = True
            
            for i in reversed(range(pos + 1, min(n + 1, pos + m + 1))):
                if a[i] == 'C':
                    continue
                elif a[i] == 'L':
                    pos = i
                    jump_to_water = False
                    break
                elif a[i] == 'W':
                    if max_water == None:
                        max_water = i

            if jump_to_water and max_water != None and k > 0:
                k -= 1
                in_water = True
                pos = max_water
            
        else:
            if a[pos + 1] == 'W' and k > 0:
                k -= 1
                pos += 1               
            elif a[pos + 1] == 'L':
                in_water = False
                pos += 1
    
        # print(pos, k)
    
    if pos == n:
        print("YES")
    else:
        print("NO")
    
    
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input()
    task(n, m, k, a)