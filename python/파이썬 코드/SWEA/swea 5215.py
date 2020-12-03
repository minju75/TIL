def dfs(i, sum_flavor=0, sum_kal = 0):
    global max_flavor
    # 칼로리 넘어가면 리턴
    if sum_kal > L:
        return
    # 최고 맛점수보다 높으면 리턴
    if max_flavor < sum_flavor:
        max_flavor=sum_flavor
    # 마지막 인덱스까지 내려왔다면 리턴
    if i == N :
        return
    flavor, kal = kal_l[i]
    # 재료를 사용했을 때
    dfs(i+1, sum_flavor+flavor, sum+kal+kal)
    # 재료를 사용하지 않았을 때
    dfs(i+1, sum_flavor, sum_kal)


t = int(input())
for tc in range(1, t+1):
    N, L = map(int, input().split())
    kal_l = [list(map(int, input().split())) for _ in range(N)]
    max_flavor = 0
    dfs(0)
    print('#{} {}'.format(t, max_flavor))
