def task(n, k):
    cntr = n
    while cntr > 0:
        if cntr % k != 0:
            if cntr == n:
                print(1)
                print(n)
                return
            elif n - cntr % k != 0:
                print(2)
                print(cntr, n - cntr)
                return
        cntr -= 1


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    task(n, k)
