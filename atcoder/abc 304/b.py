def task(n):
    if n < 1000:
        print(n)
    elif n < 1000000000:
        ans = str(n)[0:3] + '0' * (len(str(n)) - 3)
        print(ans)


n = int(input())
task(n)
