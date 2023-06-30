import sys
import math
from collections import deque

input = sys.stdin.readline


def task(n, k, x):
    ans = []
    found = False
    for i in range(1, k + 1):
        if found:
            break

        if i == x:
            continue

        if n % i == 0:
            for _ in range(n // i):
                ans.append(str(i))
            break

        for j in range(i + 1, k + 1):
            if j == x:
                continue

            if (n - i) % j == 0:
                for _ in range((n - i) // j):
                    ans.append(str(j))
                ans.append(str(i))
                found = True
                break

            elif (n - j) % i == 0:
                for _ in range((n - j) // i):
                    ans.append(str(i))
                ans.append(str(j))
                found = True
                break

    if len(ans) > 0:
        print("YES")
        print(len(ans))
        print(" ".join(ans))
    else:
        print("NO")


t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    task(n, k, x)
