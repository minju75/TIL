def dfs(r, c, total):
    dr = [0, 1]
    dc = [1, 0]
    if r == n-1 and c == n-1:
        if total < visited[r][c]:
            visited[r][c] = total
        return
    if total >= visited[-1][-1]:
        return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            dfs(nr, nc, total + num[nr][nc])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    visited = [[251]*n for _ in range(n)]
    dfs(0, 0, num[0][0])
    print('#{} {}' .format(tc, visited[-1][-1]))