from collections import deque

n, m = map(int, input().split())
r, c, s, k = map(int, input().split())
board = [[0] * (n+1) for _ in range(m+1)]
# print(board)
board[r+1][c+1] = 1
board[s+1][k+1] = 1
# print(*board)
dr = [-1, 1, 2, 2, 1, -1, -2, -2]
dc = [-2, -2, -1, 1, 2, 2, 1, -1]

def move(r, c):
    nr, nc = r, c
    for i in range(8):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr < 0 or nr >= (n+1) or nc < 0 or nc >= (m+1):
            break
        if i < 7 and nr == s and nc == k:
            pass
    return nr, nc

def bfs():
    q = deque()
    q.append(())