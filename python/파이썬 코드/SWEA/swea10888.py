t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)]
    food = []
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0 and board[r][c] != 1:
                food.append([r, c])

    for a in range(r-1, r+2)
