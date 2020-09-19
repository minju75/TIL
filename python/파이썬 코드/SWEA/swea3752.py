t = int(input())
for tc in range(1, t+1):
    n = int(input())
    score = list(map(int, input().split()))
    visit = [0] * (sum(score) + 1)  # 마지막에 중복을 제거
    q = [[0, 0]]
    while q :
        k, s = q.pop(0)
        if k == n:
            # print(s, end=' ')
            visit[s] = 1
        else:
            q.append([k+1, s])
            q.append([k+1, s+score[k]])

    # def dfs(k, s):
    #     if visit[k][s]: return
    #     visit[k][s] = 1
    #     if k == n: return
    #     dfs(k+1, s)  #k번 문제를 틀린 경우
    #     dfs(k+1, s + score[k])  #k번 문제를 맞힌 경우
    #
    # dfs(0, 0)
    print('#%d %d' %(tc, sum(visit)))