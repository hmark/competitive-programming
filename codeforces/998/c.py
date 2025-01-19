import sys
import math
from collections import deque
    
input = sys.stdin.readline
    
    
def task(n, k, x):
    cache = {}
    for xx in x:
        xxstr = str(xx)
        cache[xxstr] = cache.get(xxstr, 0) + 1
    
    ans = 0
    for valuestr in cache.keys():
        value = int(valuestr)
        find = k - value
        findstr = str(find)

        if findstr in cache:
            b = min(cache[valuestr], cache[findstr])

            if find == value:
                b //= 2

            ans += b
            cache[valuestr] -= b
            cache[findstr] -= b
    print(ans)
    
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    task(n, k, x)