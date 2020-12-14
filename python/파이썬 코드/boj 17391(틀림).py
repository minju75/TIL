def bfs(r, c):
    global total, cnt
    q = [(r, c)]
    total = board[r][c]
    board[r][c] = 0 # 방문 했으니까 0으로 변환
    dr = [0, 1] # 우하
    dc = [1, 0]
    while q:
        r, c = q.pop(0)
        if r == (m-1) and c == (n-1):
            return
        if r + total == (m - 1):
            r += total
            cnt += 1
            q.append((r, c))
        elif c + total == (n - 1):
            c += total
            cnt += 1
            q.append((r, c))
        else:
            a_max = 0
            for i in range(2):
                for j in range(1, total+1):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 0:
                        if board[nr][nc] >= a_max:
                            a_max = board[nr][nc]
                            q.append((nr, nc))
                            board[nr][nc] = 0
            cnt += 1
    return cnt


n, m = map(int, input().split()) # 세로길이 : m 가로길이 : n
board = [list(map(int, input().split())) for _ in range(n)] # 지도
cnt = 0
total = 0
# print(board)
bfs(0, 0)
print(cnt)