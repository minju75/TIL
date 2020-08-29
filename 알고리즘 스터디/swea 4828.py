t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = list(map(int,input().split()))
    for i in range(n):
        a = min(m)
        b = max(m)
        c = b-a
    print('#%d %d' %(tc, c))