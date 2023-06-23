# Dynamic Programming


def task(x, y, z, s):
    dp0 = 0
    dp1 = z

    for i in range(len(s)):
        c = s[i]
        dp0last = dp0
        dp1last = dp1

        if c == 'a':
            dp0 = min(dp0last + x, dp1last + z + x)
            dp1 = min(dp1last + y, dp0last + z + y)
        else:
            dp0 = min(dp0last + y, dp1last + z + y)
            dp1 = min(dp1last + x, dp0last + z + x)

    print(min(dp0, dp1))


x, y, z = map(int, input().split())
s = input()
task(x, y, z, s)
