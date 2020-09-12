import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    global ta, M, N
    dr = [0, 0, -1, 1] # 상하좌우
    dc = [-1, 1, 0, 0]
    table[r][c] = -1 #방문 한 것을 확인하였으니 -1로 체크
    for q in range(4):
        cr, cc = r+dr[q], c+dc[q] #현재의 좌표
        if cc <= -1 or cc >= N or cr <= -1 or cr >= M :
             continue
        if table[cr][cc] == 1:
            table[cr][cc] = 0
            dfs(cr, cc)

t = int(input())
for tc in range(1, t+1):
    M, N, K = map(int, input().split())
    table = [[0]*N for _ in range(M)]
    cnt = 0
    for i in range(K):
        a, b = map(int, input().split())
        table[a][b] = 1
    for r in range(M):
        for c in range(N):
            if table[r][c] == 1:
                cnt += 1
                dfs(r, c)
    print(cnt)
