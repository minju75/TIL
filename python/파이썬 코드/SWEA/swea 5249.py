def prim(adj, start):
    INF = float('inf')
    st = [0] * V
    weight = [INF] * V
    mst = [0] * V
    weight[start] = 0
    result = 0
    for _ in range(V):
        min_w = INF
        min_v = 0
        for i in range(V):
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        mst[min_v] = 1
        result += min_w

        for i in range(V):
            if adj[min_v][i] > 0 and not mst[i] and adj[min_v][i] < weight[i]:
                weight[i] = adj[min_v][i]
                st[i] = min_v

    return result

for tc in range(1,int(input())+1):
    V, E = map(int,input().split())
    V = V+1
    adj = [[0]*V for _ in range(V)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w


    result = prim(adj,0)
    print('#{} {}'.format(tc, result))
