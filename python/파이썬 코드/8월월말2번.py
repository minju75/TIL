def dfs(r, c):
    global madang, m, n
    dr = [0, 0, -1, 1] # 상하좌우
    dc = [-1, 1, 0, 0]
    madang[r][c] = -1 #방문 한 것을 확인하였으니 -1로 체크
    for q in range(4):
        cr, cc = r+dr[q], c+dc[q] #현재의 좌표
        if cc <= -1 or cc >= n or cr <= -1 or cr >= m :
             continue
        if madang[cr][cc] == 1:
            madang[cr][cc] = 0
            dfs(cr, cc)


t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    madang = [[0]*n for _ in range(m)]
    cnt = 0
    for i in range(k):
        a, b = map(int, input().split())
        madang[a][b] = 1
    for r in range(m):
        for c in range(n):
            if madang[r][c] == 1:
                cnt += 1
                dfs(r, c)
    print(cnt)

# 3
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
