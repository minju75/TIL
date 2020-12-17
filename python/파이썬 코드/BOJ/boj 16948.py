from collections import deque

def bfs():
    global min_cnt
    global r2, c2
    # print(x, y, cnt)
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((r1, c1))
    visited[r1][c1] = 1
    cnt = 0
    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]
    while queue:
        cnt += 1
        # print(queue)
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(6):
                nx = x + dr[i]
                ny = y + dc[i]
                if nx == r2 and ny == c2:
                    return cnt
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return -1



n = int(input())
r1, c1, r2, c2 = map(int, input().split())
chess = [[0] * n for _ in range(n)]
# min_cnt = 999
print(bfs())