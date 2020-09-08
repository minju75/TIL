import collections

def bfs(i,j,wolf,sheep):
    queue = collectons.deque()
    queue.append([i, j])
    while queue:
        i, j = queue.pop(0)
        for i in range(4):
            nr = i + dr[i]
            nc = j + dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                if fence[nr][nc] == 'v':
                    wolf += 1
                    fence[nr][nc] = '#'
                    queue.append([nr, nc])
                elif fence[nr][nc] == 'k':
                    sheep += 1
                    fence[nr][nc] == '#'
                    queue.append([nr, nc])
                elif fence[nr][nc] == '.':
                    fence[nr][nc] == '#'
                    queue.append([nr, nc])
    if wolf < sheep:
        cnt += 1
    else:
        cnt_2 += 1

R, C = map(int,input().split())
fence = [list(input()) for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0
cnt_2 = 0
for i in range(R):
    for j in range(C):
        if fence[i][j] == 'v':
            fence[i][j] = '#'
            bfs(i, j, 1, 0)
        elif fence[i][j] == 'k':
            fence[i][j] = '#'
            bfs(i, j, 0, 1)
        elif fence[i][j] == '.':
            fence[i][j] = '#'
            bfs(i, j, 0, 0)

print(*ans)
