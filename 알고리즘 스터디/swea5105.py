def bfs():
    # 시작점 찾고,
    r = 0
    c = 0
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                r,c = i,j
                break

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]


    visited = [[0] * L for _ in range(L)]
    queue = list()
    queue.append((r,c,0))
    while queue:
        #시작점으로 부터 위치정보를 얻어올때는,
        #현재 위치 받을때 같이 받아와야함.
        cr,cc,length = queue.pop(0)
        visited[cr][cc] = 1

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            #범위 내에 있으며, 방문하지 않았으면
            if 0<= nr <L and 0<= nc < L and not visited[nr][nc]:
                if maze[nr][nc] == 0:
                    queue.append((nr,nc,length+1))
                elif maze[nr][nc] == 3:
                    return length+1

    return 0


T = 10
L = 16
for t in range(T):
    tc = input()
    maze = [list(map(int,input())) for _ in range(L)]
    result = bfs()
    print("#{} {}".format(tc,result))