"1 2, 1 3, 2 4, 2 5, 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7".split()))
adj = [[0] * (N+1) for _ in range(N+1)]
for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1
visited = [0] * (N+1)
result = list()

def bfs(v):
    queue = list()
    queue.append(v)
    visited[v] = 1  # queue에 추가하면서 방문했음을 표시
    result.append(v)

    while queue:
        head = queue.pop(0)
        for i in range(len(adj[head])):
            if adj[head][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                result.append(i)

bfs(1)
print(result)