def dfs( ):
    global li, cnt, max_cnt
    dr = [1, -1, 0, 0] # 상하좌우
    dc = [0, 0, -1, 1]
    stack = []
    stack.append((i, j))
    while stack:
        cr, cc = stack.pop()
        visited[cr][cc] = 1 #visited의 0을 1로 변환해서 다녀간 걸 표시
        for q in range(4): #델타 방향 확인
            nr = cr+dr[q]
            nc = cc+dc[q]
            if 0 <= nr < n and 0 <= nc < n and li[nr][nc] == li[cr][cc] + 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                cnt += 1
    return cnt


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            cnt = 1 # 경로의 길이를 처음 잴 때
            cnt = dfs()
            if cnt > max_cnt:
                max_cnt = cnt
                start = li[i][j]
            elif cnt == max_cnt:
                if start > li[i][j]:
                    start = li[i][j]
    print('#%d %d %d' %(tc, start, max_cnt))