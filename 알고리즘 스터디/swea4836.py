t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ta = [[0]*10 for _ in range(10)]
    ta2 = [[0]*10 for _ in range(10)]
    for i in range(n):
        g1, s1, g2, s2, c = map(int,input().split())
        if c == 1:
            for j in range(g1, g2+1):
                for k in range(s1, s2+1):
                    ta[j][k] = 1
        if c == 2:
            for j in range(g1, g2+1):
                for k in range(s1, s2+1):
                    ta2[j][k] = 1
    cnt = 0
    for j in range(10):
        for k in range(10):
            if ta[j][k] == 1 and ta2[j][k] == 1 :
                cnt += 1

    print('#%d %d' %(tc, cnt))