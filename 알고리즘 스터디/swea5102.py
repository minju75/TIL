def bfs():
    queue = []
    queue.append((s, 0))
    visited = [0]*(v+1)
    visited[s] = 1

    while queue:
        now, length = queue.pop(0)
        for q in range(v+1):
            if ta[now][q] == 1 and not visited[q]:
                if q == g:
                    return length+1
                queue.append((q, length+1))
                visited[now] = 1
    return 0


t = int(input())
for tc in range(1,t+1):
    v, e = map(int,input().split())
    node = [list(map(int,input().split())) for _ in range(e)]
    ta = [[0] * (v+1) for _ in range(v+1)]
    s, g = map(int, input().split())
    while node:
        x, y = node.pop(0)
        ta[x][y] = ta[y][x] = 1

    result = bfs()
    print('#%d %d' %(tc, result))