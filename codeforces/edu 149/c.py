def task(s):
    s = [*s]

    last = ''
    for i in range(len(s)):
        if s[i] == '?':
            if last == '0':
                s[i] = '0'
            elif last == '1':
                s[i] = '1'
        last = s[i]

    last = ''
    for i in reversed(range(len(s))):
        if s[i] == '?':
            if last == '0':
                s[i] = '0'
            elif last == '1':
                s[i] = '1'
        last = s[i]

    for i in range(len(s)):
        if s[i] == '?':
            s[i] = '1'

    print(''.join(s))


t = int(input())
for i in range(0, t):
    s = input()
    task(s)
