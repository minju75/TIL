import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global arr
    deque1 = deque()
    for i in virus_num:
        deque1.extend(i)
    cnt = 0
    if S != 0:
        while deque1:
            cnt += 1
            for _ in range(len(deque1)):
                r, c = deque1.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
                        arr[nr][nc] = arr[r][c]
                        deque1.append((nr, nc))
            if cnt == S:
                return arr[X-1][Y-1]
    return arr[X-1][Y-1]


N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

virus_num = [[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        if 1<=arr[i][j]<=K:
            virus_num[arr[i][j]].append((i, j))

print(bfs())