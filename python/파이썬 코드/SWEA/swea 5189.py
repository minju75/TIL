def dfs(new):
    global num_hab, min_num
    if num_hab < min_num:
        visited[new] = 1
        if 0 not in visited:
            num_hab += num[new][0]
            if num_hab < min_num:
                min_num = num_hab
            num_hab -= num[new][0]
        else:
            for i in range(len(num)):
                if visited[i] == 0 :
                    num_hab += num[new][i]
                    dfs(i)
                    num_hab -= num[new][i]


    visited[new] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_num = 960705
    num_hab = 0
    dfs(0)
    print('#{} {}'.format(tc, min_num))