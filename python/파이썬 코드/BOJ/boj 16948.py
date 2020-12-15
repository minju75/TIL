def bfs(x, y, cnt):
    global min_cnt
    global r2, c2
    # print(x, y, cnt)
    queue = [(x, y, cnt)]
    chess[x][y] = 1
    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]
    while queue:
        # print(queue)
        x, y, cnt = queue.pop(0)
        for i in range(6):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < n and 0 <= ny < n and chess[nx][ny] == 0:
                if nx == r2 and ny == c2:
                    if min_cnt > cnt:
                        min_cnt = cnt
                else:
                    chess[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny, cnt))

            if min_cnt == 999:
                min_cnt = -1



n = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess = [[0] * n for _ in range(n)]
min_cnt = 999
bfs(r1, c1, 1)
print(min_cnt)