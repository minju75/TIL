n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
board = [['']*m for _ in range(n)]
# print(A)
# print(B)
for i in range(n):
    for j in range(m):
        board[i][j] = A[i][j] + B[i][j]

for r in board:
    print(*r)

# print(board)