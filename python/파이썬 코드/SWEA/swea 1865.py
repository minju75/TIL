def dfs(idx, answer=100):
    global max_num
    if answer <= max_num :
        return
    if idx >= N:
        max_num = answer
        return
    for i in range(N):
        if use_check[i]:
            use_check[i] = False
            dfs(idx + 1, answer * (sungong_list[idx][i]))
            use_check[i] = True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    sungong_list = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    max_num = 0
    dfs(0)
    print('#{} {:6f}'.format(t, max_num))