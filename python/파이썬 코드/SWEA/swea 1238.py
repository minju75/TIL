for tc in range(1, 11):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    g = [[] for _ in range(101)]
    for i in range(0, n, 2):
        u, v = arr[i], arr[i+1]
        g[u].append(v)

    visit = [0] * 101
    q = [s]
    visit[s] = 1

    while q :
        v = q.pop(0)
        # v 의 방문하지 않은 인접정점들
        for w in g[v]:
            if not visit[w]:
                visit[w] = visit[v] + 1
                q.append(w)

    maxidx = 1
    for i in range(2, 101):
        if visit[maxidx] <= visit[i]:
            maxidx = i

    print('#{} {}'.format(tc, maxidx))