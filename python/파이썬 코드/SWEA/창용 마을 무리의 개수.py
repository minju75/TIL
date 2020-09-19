def dfs(i):
    ta[i] = 1
    for q in range(1, n+1):
        if visited[i][q] == 1 and ta[q] == 0:
            dfs(q)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    ta = [0] * (n+1)
    visited = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        visited[a][b] = 1
        visited[b][a] = 1
    cnt = 0

    for j in range(1, n+1):
        if ta[j] == 0:
            dfs(j)
            cnt += 1

    print('#%d %d' %(tc, cnt))