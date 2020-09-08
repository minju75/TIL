# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     num = [list(map(int,input().split())) for _ in range(n)]
#     visit = [[0]*n for _ in range(n)]
#     min_num = 100000
#     b = []
#     for i in range(n*n):
#         if num[0][i] < min_num:
#             min_num = num[0][i]
#             b.append(num[0][i])
#         for x in range(i+1,n):
#             for y in range(n):
#                 visit[x][i] = 1
#                 if visit[x][y] == 0 and num[x][y] < min_num :
#                     min_num = num[x][y]
#                     b.append(num[x][y])
#                     continue
#
#     print('#%d %d' %(tc, sum(b)))


def dfs(r,total):
    global min_num
    if r >= n:
        if total < min_num:
            min_num = total
    elif total > min_num:
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                dfs(r + 1, total + num[r][i])
                visited[i] = 0
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    min_num = 100000
    dfs(0,0)
    print('#%d %d' %(tc, min_num))

