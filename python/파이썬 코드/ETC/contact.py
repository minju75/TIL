for tc in range(1, 11):
    n, s = map(int,input())
    arr = list(map(int,input().split()))


    g = [[0] * 101 for _ in range(101)] # 정점번호 1~100
    for i in range(0, n, 2): #arr[i] --> arr[i+1]
        g[arr[i]][arr[i+1]] = 1

    visit = [0] * 101
    q = [s]
    visit[s] = 1

    while q :
        v = q.pop(0)
        for w in range(1, 101):
            if g[v][w] and not visit[w] :
                visit[w] = visit[v] + 1
                q.append(w)

    ans = 1
    for i in range(2, 101):
        if visit[ans] <= visit[i]
            ans = i
    print(ans)