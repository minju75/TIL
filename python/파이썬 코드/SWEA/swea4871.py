def check(s):
    global stack
    global g

    for i in range(1,v+1):
        if board[s][i] == 1:
            if i == g:
                return 1

            check(i)
    return 0

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    board = [[0]*(v+1) for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        board[a][b] = 1

    s, g = map(int, input().split())
    stack = []