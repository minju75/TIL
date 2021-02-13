def bfs(h, c, r):
    global cnt
    visited = [[[0] * m for _ in range(n)] for _ in range(h)]
    visited[h][c][r] = 1
    q.append((h, c, r))
    while q:
        cnt += 1
        h, c, r = q.pop(0)
        visited[h][c][r] = 1
        for p in range(6):
            nr = r + dr[p]
            nc = c + dc[p]
            nh = h + dk[p]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nh < h and visited[nh][nr][nc] == 0:
                cnt += 1
                visited[nh][nc][nr] = 1
                q.append((nh, nr, nc))
                return cnt

    return -1

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# print(tomato)
cnt = 0

dr = [0, 0, -1, 1, 0, 0] # 가로
dc = [-1, 1, 0, 0, 0, 0] # 세로
dk = [0, 0, 0, 0, 1, -1] # 위,아래

q = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                result = bfs(k, i, j)

print(result)

