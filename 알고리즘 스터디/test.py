def comb(selected, idx, cnt):
    if cnt == T:
        a = -1
        b = -1
        for i in range(N):
            if selected[i] == 1:
                if a == -1:
                    a = i
                else:
                    b = i
        print(a, b)

        return
    if idx >= N - 1:
        return

    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)
    return

t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_cnt = float('inf')
    selected = [0] * n
    comb(selected, 0 , 0)
    for i in range(0, len(result), 2):
        cnt = 0
        for w in range(0, i + 1):
            for k in range(M):
                if flag[w][k] != 'W':
                    cnt += 1
        for b in range(i + 1, j + 1):
            for k in range(M):
                if flag[b][k] != 'B':
                    cnt += 1
        for d in range(j + 1, N):
            for s in range(M):
                if flag[d][s] != 'R':
                    cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
    print('#{} {}'.format(tc, min_cnt))
