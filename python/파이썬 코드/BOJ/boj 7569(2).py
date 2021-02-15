from collections import deque

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def bfs():
    global tomato_box
    deque1 = deque()
    zero_cnt = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_box[i][j][k] == 1:
                    deque1.append((i, j, k, 0))
                elif tomato_box[i][j][k] == 0:
                    zero_cnt += 1

    if zero_cnt == 0:
        return 0

    cnt = 0
    while deque1:
        ch, cr, cc, cnt = deque1.popleft()
        if len(deque1)==0:
            ans = cnt
        for i in range(6):
            nr = cr + dr[i]
            nc = cc + dc[i]
            nh = ch + dh[i]
            if 0<=nr<N and 0<=nc<M and 0<=nh<H and tomato_box[nh][nr][nc]==0:
                tomato_box[nh][nr][nc] = 1
                deque1.append((nh, nr, nc, cnt+1))

    for i in tomato_box:
        for j in i:
            if 0 in j:
                return -1
    return ans


M, N, H = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
print(bfs())