t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    num = list(map(int,input().split()))
    for i in range(m+1):
        a = num[0]
        num.pop(0)
        num.append(a)
    print('#%d %d' %(tc,num[n-1]))