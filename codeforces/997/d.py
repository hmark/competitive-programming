import sys
import math
from collections import deque

input = sys.stdin.readline

def task(n, a):
    ans = 0

    for x in range(1, 11):
        b = [1 if a[i] > x else -1 for i in range(n)]
        sum_val = n
        pref = [0] * n

        for i in range(n):
            pref[i] = sum_val
            sum_val += b[i]

        cnt = [0] * (2 * n + 1)
        sum_val = n
        j = 0

        for i in range(n):
            if a[i] == x:
                while j <= i:
                    cnt[pref[j]] += 1
                    j += 1

            sum_val += b[i]
            ans += cnt[sum_val]

    ans = n * (n + 1) // 2 - ans
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
