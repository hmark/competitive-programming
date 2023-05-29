def task(n, s):
    last = ''
    mx = 1
    for c in s:
        if c != last:
            last = c
            curr = 2
        else:
            curr += 1

        mx = max(curr, mx)

    print(mx)


t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    task(n, s)
