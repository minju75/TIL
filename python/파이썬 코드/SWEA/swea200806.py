t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    ta = [list(map(int,input().split())) for _ in range(n)]
    max_total = 0
    # print(ta)
    for i in range(n-m+1):
        for j in range(n-m+1):
            r = 0
            for a in range(m):
                for b in range(m):
                    r += ta[i+a][j+b]
                if max_total < r:
                    max_total = r
    print('#%d %d' %(tc, max_total))