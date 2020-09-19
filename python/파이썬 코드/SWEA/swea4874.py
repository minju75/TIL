t = int(input())
for tc in range(1,t+1):
    num = list(input().split())
    b = []
    ans = 0
    for i in range(len(num)-1):
        if num[i] != '+' and num[i] != '-' and num[i] != '*' and num[i] != '/':
            b.append(num[i])
        else:
            try:
                d, e = int(b.pop()), int(b.pop())
                if num[i] == '+':
                    r = e+d
                elif num[i] == '-':
                    r = e-d
                elif num[i] == '*':
                    r = e*d
                elif num[i] == '/':
                    r = e//d
                b.append(r)

            except:
                ans = -1
    if ans == -1 or len(b) >= 2:
        print('#%d' %tc, "error")
    else:
        print('#%d %d' %(tc, int(b.pop())))