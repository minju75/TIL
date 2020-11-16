def snail(cr, cc):
    global k, n
    global board
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    while board[n//2][n//2] == 0:
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            while 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                k -= 1
                board[nr][nc] = k
                nr += dr[i]
                nc += dc[i]
            nr -= dr[i]
            nc -= dc[i]
            cr,cc=nr,nc



n = int(input())
m = int(input())
board = [[0]*n for _ in range(n)]
k = n*n
r, c = 0, 0
board[r][c] = k
snail(r, c)
for i in board:
    print(*i)

for i in range(n):
    for j in range(n):
        if board[i][j] == m:
            print(i+1, j+1)
