def task(n, s):
    ans = []
    curr = 0
    last = None
    main = None
    over = False
    under = False

    for c in s:
        if c == '(':
            curr += 1
        else:
            curr -= 1

        if not main:
            if curr > 0:
                main = '('
            else:
                main = ')'

        if curr > 0:
            over = True
            if main == '(':
                last = '1'
            else:
                last = '2'
        elif curr < 0:
            under = True
            if main == ')':
                last = '1'
            else:
                last = '2'

        ans.append(last)

    if curr != 0:
        print(-1)
        return

    print(2 if over and under else 1)
    print(' '.join(ans))


t = int(input())
for i in range(0, t):
    n = int(input())
    s = input()
    task(n, s)
