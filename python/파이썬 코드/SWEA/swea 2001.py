T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    my_map = [tuple(map(int, input().split())) for _ in range(N)]
    result = -1
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            sub_res = 0
            for dr in range(M):
                for dc in range(M):
                    sub_res += my_map[r+dr][c+dc]
            if result < sub_res:
                result = sub_res
    print('#{} {}'.format(test_case, result))