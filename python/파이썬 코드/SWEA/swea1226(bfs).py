def bfs(cr, cc):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    queue = []
    cnt = 0
    queue.append((cr, cc, cnt))
    visited = [[0] * n for _ in range(n)]
    while queue:
        # print(queue)
        cr, cc, cnt = queue.pop(0)
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                if maze[nr][nc] == '0':

                    visited[nr][nc] = 1
                    queue.append((nr, nc, cnt + 1))
                elif maze[nr][nc] == '3':
                    return cnt
    return 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maze = [list(input()) for _ in range(n)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                a = bfs(i, j)
    print('#%d %d' % (tc, a))