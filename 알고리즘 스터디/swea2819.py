# def dfs(index, r, c, total):
#     dr = [1, 0, -1, 0] #상우하좌
#     dc = [0, 1, 0, -1]
#     total += table[r][c]
#     if index == 6:
#         result.append(total)
#         return
#     for i in range(4):
#         if 0 <= r+dr[i] < 4 and 0 <= c+dc[i] < 4: #벽 피하기
#             dfs(index+1, r+dr[i], c+dc[i], total)
#
# t = int(input())
# for tc in range(1, t+1):
#     table = [list(map(str,input().split())) for _ in range(4)]
#     result = []
#     for r in range(4):
#         for c in range(4):
#             dfs(0,r,c,"")
#
#     print('#%d %d' %(tc, len(set(result))))
arr = [1, 2, 3, 4]
n = 4
selected = [0] * n
t = 2 # 원하는 조합의 요소 개수
#selected는 어떤 요소가 선택되었는지 표시하는 배열
#index : 요소의 index
#cnt : 선택된 요소의 개수
def comb(selected, idx, cnt):
    global min_cnt
    if cnt == t:
        # 내가 원하는 개수만큼의 요소를 선택했음
        # print(selected)
        # 내가 원하는 조합을 만들었으니
        # 원하는 계산은 여기서 한다!
        return
        a = b = -1
        for i in range(n):
            if selected[i] == 1:
                if a == -1:
                    a = i
                else:
                    b = i
        print(a, b)
        for i in range(0,a+1):
            for k in range(m):
                for k in range(M):
                    if flag[i][k] != 'W':
                        cnt += 1
        for i in range(a+1, b+1):
            for k in range(M):
                if flag[i][k] != 'W':
                    cnt += 1
        for i in range(b+1, n):
            for k in range(M):
                if flag[i][k] != 'W':
                    cnt += 1

            return
    if idx >= N - 1:
        return

        # 요소를 선택하거나/ 선택하지 않거나 모든 경우의 수 감안

    selected[idx] = 1  # idx에 해당하는 요소를 포함
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)
    return  # 내가 할 수 있는 모든 경우의 수 다 봤으니 내 턴을 종료한다.

comb(selected, 0, 0)


    # 요소를 선택하거나 선택하지 않거나 모든 경우의 수를 감안

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flag = [input() for _ in range(N)]
    INF = float('inf') #많이 큰 수를 표현할 때 사용
    min_cnt = INF
print('#%d %d' %(tc, min_cnt))

