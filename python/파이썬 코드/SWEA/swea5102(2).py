t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    board = [[0]*(v+1) for _ in range(v+1)]
    for i in node:
        board[i[0]][i[1]] = 1

    stack = []

    while True:
        cnt = 0
        if 1 in board[s] :
            k = board[s].index(1)
            board[s][k] = 0
            stack.append(s)
            s = k
            cnt += 1
            if k == g:
                cnt += 1
                break

        else:
            if stack == []:
                cnt = 0
                break

            else:
                s = stack.pop(0)

    print('#%d %d' %(tc, cnt))