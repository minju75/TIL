def dfs():
    global ladder
    dr = [0,0,1]
    dc = [-1,1,0]
    for i in range(100):
        if ladder[0][i]==1:
            visited = [[0]*100 for _ in range(100)]
            stack = []
            stack.append((0,i))
            while stack:
                cr, cc = stack.pop()
                visited[cr][cc] = 1
                for d in range(3):
                    nr = cr+dr[d]
                    nc = cc+dc[d]
                    if 0 <= r < 100 and 0 <= c < 100 and visited[nr][nc] == 0:
                        if ladder[nr][nc] == 1 :
                            stack.append((nr,nc))
                            break
                        elif ladder[nr][nc] == 2:
                            return i

t = 10
for tc in range(1,11):
    n = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    result = dfs()
    print('#%d %d' %(tc, result))
