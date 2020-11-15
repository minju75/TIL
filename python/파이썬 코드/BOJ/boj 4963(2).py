import sys
sys.setrecursionlimit(10000)

dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)
def dfs(x, y):
    visited[x][y] = 1
    for q in range(8):
        nx, ny = x + dx[q], y + dy[q]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if map_li[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    map_li = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if map_li[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)


