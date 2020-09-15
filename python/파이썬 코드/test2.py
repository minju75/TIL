t = int(input())
for tc in range(1, t+1):
    n, m, d = map(int,input().split())
    ta = [[0]*n for _ in range(n)] # 먼저 n*n 배열로 이루어진 2차원 리스트 생성
    a = n//2
    b = []

    for i in range(0, a+1): # ta 안에 들어가야 할 숫자 list
        b.append(m+(d*i))

    for i in range(n):
        for j in range(n):
            ta[i][j] = m

    for x in range(a , -1, -1):  # 중심에서 바깥쪽으로 채워넣기
        for i in range(a-x, a+1+x):
            for j in range(a-x, a+1+x):
                if ta[i][j] != 0 :
                    ta[i][j] = b[x]
    #print(ta)
    for r in ta:
        print(*r)
    # for i in range(n):
    #     q = sum(ta[i]) #행의 합 구하기
    #     print(q, end=" ")
    # print()