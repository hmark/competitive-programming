def task(n, s):
    table = {}
    for i in range(n-1):
        m = s[i:i+2]
        table[m] = True
    print(len(table))


t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    task(n, s)
