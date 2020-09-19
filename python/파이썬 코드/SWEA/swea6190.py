t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int,input().split()))
    li = []
    for i in range(n-1):
        for j in range(i+1, n):
            a = num[i]*num[j]
            if a >= 10:
                b = str(a)
                for q in range(len(b)-1):
                    if b[q] > b[q+1]:
                        result = -1
                    else:
                        li.append(a)
                    result = max(li)
    # print(li)
    print('#%d %d' %(tc, result))