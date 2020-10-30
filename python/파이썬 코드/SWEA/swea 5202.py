t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]
    num = sorted(li, key=lambda x : x[1])
    # print(num)
    # print(num.pop(0))
    end = num[0][1]
    cnt = 1
    # print(end)
    for i in range(n-1):
        if end <= num[i+1][0]:
            end = num[i+1][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))eee