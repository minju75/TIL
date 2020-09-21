def bfs(i, j):
    global total, n, m, k, board
    dr = [1, 0, -1, 0]  # 우하좌상(가로)
    dc = [0, -1, 0, 1] # 우하좌상(세로)
    queue = []
    queue.append((i, j)) # 전체 합계를 구해야하는 것이기에 queue 라는 리스트에 cr, cc을 append 해 줌
    visited = [[0]*m for _ in range(n)] # 방문 지점을 표시할 2차원 리스트 visited 만들어 놓기
    while queue :
        cr, cc = queue.pop(0)  # bfs를 사용할 것이기 때문에 선입선출의 개념 활용
        visited[cr][cc] = 1 # 방문 한 곳이기에 1로 체크
        num = [] # 합계를 넣어서 비교해 줄 리스트
        total += board[cr][cc]  # 처음 시작 값을 total에 더해주고 시작
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i] # nr, nc는 새로운 델타의 요소가 더해진 새로운 방향
            if 0 <= nr < cr+k and 0 <= nc < cc+k and cr+k <= m and cc+k <= n and visited[nr][nc] == 0: # 방문할려는 곳이 현재 좌표에서 k를 더한 값보다 작으며 방문하지 않았다는 조건 설정
                if board[nr][nc] != 0:
                    visited[nr][nc] = 1  # 방문하였기 때문에 방문 표시
                    total += board[nr][nc] # 합계를 구해야하기 때문에 total 에다가 더해줌
                    queue.append((nr, nc))  # 방문한 좌표인 nr, nc는 다시 queue에 append

                bfs(nr, nc)

                if nr == cr and nc == cc: # nr과 nc가 처음의 좌표로 돌아왔으면 break
                    num.append(total)

    return max(num)-min(num) # 최댓값과 최소값을 차이를 구해서 return


t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    # print(board)
    for i in range(m):
        for j in range(n):
            if board[i][j] != 0: # 특정 범위가 아닌 전체를 탐색해야하기 때문에 0이 아닐 경우에
                result = bfs(i, j)    # bfs 함수로 넣어줌

        print('#%d %d' %(tc, result))