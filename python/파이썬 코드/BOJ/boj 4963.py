import sys
sys.setrecursionlimit(100000)

def dfs(r, c):
    map_li[r][c] = 0
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0 <= nr < w and 0 <= nc < h and visited[nr][nc] == 0:
            if map_li[nr][nc] == 1:
                map_li[nr][nc] == 0
                visited[nr][nc] = 1
                dfs(nr, nc)
        else:
            continue

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    map_li = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(w):
        for j in range(h):
            if map_li[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
