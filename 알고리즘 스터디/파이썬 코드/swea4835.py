t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    q = []
    for i in range(n-m+1):
        q.append(sum(a[i:i+m]))
        # print(q)
    a = max(q)
    b = min(q)
    #print(a, b)
    print('#%d %d' %(tc, (a-b)))