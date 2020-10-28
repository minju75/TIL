t = int(input())
for tc in range(1, t+1):
    player_1 = [0] * 12
    player_2 = [0] * 12
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        if i % 2:
            player_2[tmp[i]] += 1
        else:
            player_1[tmp[i]] += 1
    dic = {1 : player_1, 2: player_2}
    cnt = 100
    result = 0
    for j in range(1, 3):
        c = dic[j]
        # print(tc,j,c)
        i = 0
        while i < 10:
            if c[i] >= 3:
                c[i] -= 3
                if j == 1:
                    cnt = i
                if j == 2 and cnt > i:
                    cnt = i
                    result = 2
                else:
                    result = 1
            if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2]>= 1:
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                if j == 1:
                    cnt = i
                if j == 2 and cnt > i:
                    cnt = i
                    result = 2
                else:
                    result = 1
            i += 1
    print(f'#{tc} {result}')