import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    visited[r][c] = 1
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for q in range(4):
        nr, nc = r + dr[q], c + dc[q]
        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue
        if visited[nr][nc] == 0 and board[nr][nc] == '#':
            dfs(nr, nc)

t = int(input())
for tc in range(t):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
