def bfs():
    r = 0
    c = 0
    for i in range(tc):
        for j in range(tc):
            if maze[i][j] == 2:
                r,c = i,j
                break

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]


    visited = [[0] * tc for _ in range(tc)]
    queue = list()
    queue.append((r,c,0))
    while queue:
        cr,cc,length = queue.pop(0)
        visited[cr][cc] = 1

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<= nr <tc and 0<= nc < tc and not visited[nr][nc]:
                if maze[nr][nc] == 0:
                    queue.append((nr,nc,length+1))
                elif maze[nr][nc] == 3:
                    return length

    return 0


T = int(input())
for t in range(1,T+1):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(tc)]
    result = bfs()
    print("#{} {}".format(t,result))