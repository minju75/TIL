# 연습문제 1 -DFS
# 다음은 연결되어 있는 두개의 정점 사이의 간선을 순서대로 나열 해 놓은 것 이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.
# 시작정점을 1로 하시오.

"1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
N = 7
en = 8
edges = list(map(int,input().split()))
adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(0,len(edges),2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1

visited = [0] * (N+1)
result = list()
def dfs(v):
    global result
    if visited[v]:
        return

    result.append(v)
    visited[v] = 1
    for i in range(len(adj[v])):
        if adj[v][i] == 1:  # [0,0,0,0,1,1,0,0]
            dfs(i)

dfs(1)
print(result)