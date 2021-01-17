import sys
from collections import deque

def bfs(v):
    global cnt
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for n in arr[v]:
            if visited[n] == 0:
                visited[n] = 1
                cnt += 1
                queue.append(n)


T = int(sys.stdin.readline())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    # arr = [[0] * (N+1) for _ in range(N+1)]
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    visited[0] = 1
    cnt = 0
    queue = deque([])
    for m in range(M):
        i, j = map(int, sys.stdin.readline().split())
        arr[i].append(j)
        arr[j].append(i)

    for i in range(N):
        if visited[i] == 0:
            bfs(1)

    print(cnt)