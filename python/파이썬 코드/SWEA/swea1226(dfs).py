def dfs(cr, cc):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0]*16 for _ in range(16)]
    stack = []
    stack.append((cr, cc))
    while stack:
        # print(stack)
        cr, cc = stack.pop()

        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0:
                if miro[nr][nc] == '0':
                    stack.append((nr, nc))
                    visited[nr][nc] = '1'
                if miro[nr][nc] == '3':
                    return 1

    return 0


for tc in range(1, 11):
    n = int(input())
    miro = [list(input()) for _ in range(16)]
    # print(miro)
    for i in range(16):
        for j in range(16):
            if miro[i][j] =='2':
                a = dfs(i, j)

    print('#%d %d' %(tc, a))