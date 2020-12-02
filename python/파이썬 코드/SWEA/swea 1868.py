from collections import deque
# 왼상 부터 시계방향으로 8방향
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if game[nr][nc] == 0 :
                    queue.append((nr, nc))

def mine_check(r, c):
     cnt = 0

     for i in range(8):
         nr = r + dr[i]
         nc = c + dc[i]
         if nr < 0 or nr >= N or nc < 0 or nc >= N:
             continue
         if game[nr][nc] == "*" :
             cnt += 1
     return cnt


for tc in range(1, int(input())+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]

    # 내 주변의 지뢰 수로 2차원 리스트를 갱신
    zero_list = []
    for i in range(N):
        for j in range(N):
            if game[i][j] == ".":
                game[i][j] = mine_check(i, j)
            if game[i][j] == 0:
                zero_list.append((i, j))

    ans = 0
    visited = [[False] * N for _ in range(N)]
    for r, c in zero_list:
        if visited[r][c] : continue
        BFS(r, c)
        ans += 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game[i][j] != "*":
                ans += 1

    print('#{} {}'.format(tc, ans))
