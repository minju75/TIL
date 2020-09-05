def dfs(i,j) :
    global result
    if miro[i][j] == '3':
        result = 1
        return
    visited.append((i,j))
    for d in range(0,4):
        cr = i + dr[d]
        cc = j + dc[d]
        if 0 <= cr < n and 0 <= cc < n and miro[i][j] != '1' and (cr,cc) not in visited:
            dfs(cr,cc)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    miro = []
    for j in range(0,n):
        mi = str(input())
        miro.append(mi)
        #miro = [list(map(str, input().split())) for _ in range(n)]
        if '2' in mi:
            i_start = j
        if '3' in mi:
            i_end = j
    j_start = miro[i_start].find('2')
    j_end = miro[i_end].find('3')

    visited = []

    j_cur = j_start
    i_cur = i_start

    dr = [0,0,-1,1] #하좌상우
    dc = [1,-1,0,0]
    ans = 0
    dfs(i_start, j_start)

    if ans == 1:
        print("#%d" %tc, 1)
    else :
        print("#%d" %tc, 0)