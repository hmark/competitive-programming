def task(n, a):
    mx = max(a)
    mxi = a.index(mx)

    if n == 1:
        print(1)
        return

    if mxi == 0:
        mx = max(a[1:])
        mxi = a.index(mx)
        if mxi == n - 1:
            l = mxi
            r = l
        else:
            l = mxi - 1
            r = l
    elif mxi == n - 1:
        r = n - 1
        l = r
        while l > 0 and a[l - 1] > a[0]:
            l -= 1
    else:
        r = mxi - 1
        l = r
        while l > 0 and a[l - 1] > a[0]:
            l -= 1

    # print(l, r)
    results = a[r+1:] + list(reversed(a[l:r+1])) + a[0:l]
    print(' '.join(map(str, results)))


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
