t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    li = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                x = 0
                for k in range(j, n):
                    if board[i][k] != 0:
                        x += 1
                    else:
                        break
                y = 0
                for k in range(i, n):
                    if board[k][j] != 0:
                        y += 1
                    else:
                        break

                for k in range(i, i+y):
                    for f in range(j, j+x):
                        board[k][f] = 0

                li.append([x*y, y, x])
                li.sort(key=lambda x : (x[0], x[1]))
    p = []
    for i in range(len(li)):
        p.append(li[i][1])
        p.append(li[i][2])
    print('#%d %d' %(tc, len(li)), end=' ')
    print(*p)