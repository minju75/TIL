def bfs(i):
    queue = []
    queue.append(i)
    visited[i] =1
    while queue:
        i = queue.pop(0)
        for i in range(n):
            if visited





t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    list = [[0] for _ in range(n)]
    visited = [0 for _ in range(n+2)]
    cnt = 0
    for i in range(m): # 연결된 곳 표시
        a, b = map(int, input().split())
        list[a] = b
        list[b] = a
    for i in range(n):
        if visited[i] == 0: # 방문하지 않은 i에서 시작
            bfs(i) # 깊이 탐색 시작
            cnt += 1
