from collections import deque

dr = [1, 0]
dc = [0, 1]

def bfs(r, c, b, ct):
    global min_cnt
    deque1 = deque()
    deque1.append((r, c, b, ct))
    while deque1:
        cr, cc, boost, cnt = deque1.popleft()
        for i in range(2):
            for j in range(1, boost+1):
                nr = cr + dr[i]*j
                nc = cc + dc[i]*j
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc]==0:
                    if nr == N-1 and nc == M-1:
                        if min_cnt > cnt:
                            min_cnt = cnt
                    else:
                        deque1.append((nr, nc, arr[nr][nc], cnt+1))
                        visited[nr][nc] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
min_cnt = 999
bfs(0, 0, arr[0][0], 1)
print(min_cnt)