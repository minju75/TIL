t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    # ta = [([0] * (n)) for _ in range(n)]
    m = [list(map(int,input().split())) for _ in range(n)] # 가로

    # 세로 리스트 받기
    x = []
    for p in range(n):
        se = []
        for i in range(n):
            se.append(m[i][p])
        x.append(se)

    cnt = 0
    for o in range(n):
        for j in range(n-k+1):
            if m[o][j:j+k] == [1] * k:
                if j+k == n:
                    if j-1 >= 0 :
                        if m[o][j-1] == 0 :
                            cnt += 1
                    else :
                        cnt += 1
                elif m[o][j+k] == 0 :
                    if j - 1 >= 0:
                        if m[o][j - 1] == 0:
                            cnt += 1
                    else:
                        cnt += 1
            else:
                continue
    # print(cnt)

    for e in range(n):
        for s in range(n - k + 1):
            if x[e][s:s + k] == [1] * k:
                if s + k == n:
                    if s - 1 >= 0:
                        if x[e][j - 1] == 0:
                            cnt += 1
                    else:
                        cnt += 1
                elif x[e][s + k] == 0:
                    if s - 1 >= 0:
                        if x[e][s - 1] == 0:
                            cnt += 1
                    else:
                        cnt += 1
            else:
                continue
    print('#%d %d' %(tc, cnt))

