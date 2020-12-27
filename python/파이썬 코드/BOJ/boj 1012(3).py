def dfs(cr, cc):
    dr = [1, 0, -1, 0]
    dc = [0,  1, 0, -1]
    table[r][c] = 0
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nc < n and 0 <= nr < m and table[nr][nc] == 1:
            table[nr][nc] = 0
            dfs(nr, nc)


t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    table = [[0]*n for _ in range(m)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        table[x][y] = 1

    for r in range(m):
        for c in range(n):
            if table[r][c] == 1:

                dfs(r, c)
                cnt += 1

    print(cnt)