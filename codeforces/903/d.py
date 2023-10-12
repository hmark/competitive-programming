import sys
import math
from collections import deque

input = sys.stdin.readline


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def task(n, a):
    if n == 1:
        print("YES")
        return

    # print(n, a)
    cache = {}
    for val in a:
        # print(prime_factors(val))
        for prime in prime_factors(val):
            if not prime in cache:
                cache[prime] = 0
            cache[prime] += 1

    # print(cache)
    for key, value in cache.items():
        # print(key, value)
        if value == 1 or value % n != 0:
            print("NO")
            return
    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
