def dfs(r, c):
    global m, n, board, cnt, a
    dr = [0, 1, 0, -1]        # 상우하좌로 움직이는 방향
    dc = [1, 0, -1, 0]
    board[r][c] = -1 # 방문한 부분은 -1 로 변환
    stack = []
    for d in range(4):
        cr, cc = r+dr[d], c+dc[d]          # 현재의 좌표
        # print(cr, cc)
        if cc <= -1 or cc >= m or cr <= -1 or cr >= n : #모서리에 가거나 n,m 을 넘어가지 않도록 범위 설정
            continue
        if board[cr][cc] > a or not board[cr][cc]:    # 최솟값으로 설정했던 부분보다 크거나 값이 존재하지 않는다면(벽면이라면)
            stack.append((cr, cc))  # stack 이라는 리스트에 넣어주기
            board[cr][cc] = -1    # 방문한 부분이기 때문에 -1로 바꿔주기
            dfs(cr, cc)  # 다시 dfs 시작
        # if not board[cr][cc] :
        #     stack.append((cr, cc))
            if len(stack) > 1:  # stack의 갯수가 2개를 넘는다면 빛을 보지 못하는 면이 2군데가 넘는 것 이기 때문에
                cnt += 2        # cnt 에 +1 해주기기


t = int(input()) # 입력 받을 testcase의 갯수
for tc in range(1, t+1):
    n, m = map(int, input().split()) # n : 가로, m : 세로
    board = [list(map(int,input().split())) for _ in range(n)] # 나무가 심어져 있는 정원 만들기
    b = []
    cnt = 4 # 모서리에 있는 나무들은 2면에서 빛을 못 받기 때문에 모서리의 갯수 cnt 하고 시작
    for i in range(n):
        b.append(min(board[i]))
        a = min(b) # 정원에 있는 나무의 최솟값 찾기
        garden = []
        # print(a)
        for r in range(n):
            for c in range(m):
                if board[r][c] == a:  # 최솟값을 가진 나무의 위치 찾아서
                    dfs(r, c) # 깊이 탐색 시작

    print('#%d %d' %(tc, cnt))