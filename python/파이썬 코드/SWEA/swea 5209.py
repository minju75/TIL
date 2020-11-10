def dfs(idx, _sum):
    global answer
    if _sum >= answer:
        return
    if idx == n:
        answer = _sum
    for i in range(n):
        if visited[i] == 1:
            visited[i] = 0
            dfs(idx+1, _sum + factory[idx][i])
            visited[i] = 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    visited = [1 for _ in range(n)]
    answer = 9999999
    dfs(0, 0)
    print('#{} {}'.format(tc, answer))
