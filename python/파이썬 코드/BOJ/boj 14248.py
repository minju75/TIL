def bfs(s):
    global cnt
    visited = [0] * (n+1)
    visited[s] = 1 # 방문 체크
    queue = []
    queue.append(s)
    dc = [-1, 1] # 왼, 오 로만 이동
    while queue:
        c = queue.pop(0)
        for i in range(2):
            nc = c + dc[i]*stone[c]
            if 0 < nc <= n and visited[nc] == 0 :
                visited[nc] = 1
                cnt += 1
                queue.append(nc)


n = int(input())
stone = [0]+list(map(int, input().split()))
start = int(input())
# print(stone)
cnt = 1
bfs(start)
print(cnt)