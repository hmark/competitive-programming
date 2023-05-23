def task(n, a):
    evens = 0
    odds = 0
    aa = sorted(a)

    for i in range(n):
        if a[i] % 2 == 0:
            evens += 1
        else:
            odds += 1

    if evens > 0 and odds == 0:
        print("YES")
    elif aa[0] % 2 == 1:
        print("YES")
    else:
        print("NO")


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
