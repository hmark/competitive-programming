def task(n, s, t):
    for i in range(n):
        if s[i] == t[i]:
            continue
        elif (s[i] == '1' or t[i] == '1') and (s[i] == 'l' or t[i] == 'l'):
            continue
        elif (s[i] == '0' or t[i] == '0') and (s[i] == 'o' or t[i] == 'o'):
            continue
        else:
            print("No")
            return
    print("Yes")


n = int(input())
s = input()
t = input()
task(n, s, t)
