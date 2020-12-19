def bfs(x, y):
    global visited
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = [[x, y]]
    visited[x][y] = 1
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

bfs(0, 0)
print(visited[n-1][m-1])