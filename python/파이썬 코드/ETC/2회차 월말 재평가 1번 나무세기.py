def dfs(r, c, num):
    global board, cnt
    ans = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            # print(r, c, nr, nc)
            if num >= board[nr][nc]:
                ans += 1
    if ans <= 2:
        cnt += 1

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            dfs(i, j, board[i][j])


    print('#%d %d' %(tc, cnt))