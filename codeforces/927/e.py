import sys
import math
from collections import deque


def task(n, s):
    total = 0
    dp = []
    ans = []

    for c in s:
        total += int(c)
        dp.append(total)

    carry = 0
    for i in reversed(range(n)):
        digit = (carry + dp[i]) % 10
        carry = (carry + dp[i]) // 10
        ans.append(str(digit))

    if carry != 0:
        ans.append(str(carry))

    print("".join(reversed(ans)).lstrip('0'))


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    task(n, s)
