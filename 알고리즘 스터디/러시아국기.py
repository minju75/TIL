target = ['w', 'b', 'r']
def rusia(index, color, cnt):

    if result <= cnt:
        return
    if idx >= N-1:
        result = cnt
        return
    for i in range(color, min(3, color+2)):
        temp = 0
        if idx >= N-2 and i == 0:
            continue
        for j in flag[idx]:
            if j != target[i]:
                temp += 1
        rusia(idx+1, i, cnt+temp)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    flag = [(str,input().split()) for _ in range(N)]
    result = 3000
    rusia(1, 0, 0)
    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            # 여기서 세개의 영역으로 구분할 수 있음
            # 0~i, i+1~j, j+1~끝
            cnt = 0
            # 흰색 영역 순회하면서 바꿔야할 개수 세기
            for w in range(0, i + 1):  # i가 흰색영역의 끝이니 i를 포함해야함
                for k in range(M):
                    if flag[w][k] != 'W':
                        cnt += 1
            # 파란 영역 순회하면서 바꿔야할 개수 세기
            for b in range(i + 1, j + 1):
                for k in range(M):
                    if flag[b][k] != 'B':
                        cnt += 1
            # 빨간 영역 순회하면서 바꿔야할 개수 세기
            for r in range(j + 1, N):
                for k in range(M):
                    if flag[r][k] != 'R':
                        cnt += 1

            if cnt < min_cnt:
                min_cnt = cnt
    print('#%d %d' %(tc, result))
