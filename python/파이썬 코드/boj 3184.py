def bfs(r, c):
    dr = [-1, 0, 1, 0] # 상우하좌
    dc = [0, 1, 0, -1]
    queue = [(r, c)]
    visited[r][c] = 1
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < r and 0 <= nc < n and visited[nr][nc] == 0:
                visited


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
# print(arr)

for i in range(c):
    for j in range(r):
        if arr[i][j] == 'o' or arr[i][j] == 'v':
            bfs(i, j)