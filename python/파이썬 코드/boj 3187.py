import sys
input = sys.stdin.readline
def bfs(x, y):
    visited[x][y] = 1 # 방문표시
    q = [[x, y]] # q에 append
    dx = [1, 0, -1, 0] # 4방향(상우하좌)
    dy = [0, 1, 0, -1] # 4방향(상우하좌)
    v_cnt = 0 # 늑대의 수
    k_cnt = 0 # 양의 수
    while q :
        x, y = q.pop(0)
        if board[x][y] == 'v': # 늑대라면
            v_cnt += 1 # 늑대의 수에다가 1 증가
        elif board[x][y] == 'k': # 양이라면
            k_cnt += 1  # 양의 수에다가 1 증가
        for i in range(4):
            nx = x+dx[i] # 새로운 행
            ny = y+dy[i] # 새로운 열
            if 0 <= nx < r and 0 <= ny < c : # 범위를 벗어나지 않는다면
                if board[nx][ny] != '#' and visited[nx][ny] == 0: # 새로운 좌표의 위치가 울타리가 아니면서 방문한 적이 없을 때
                    visited[nx][ny] = 1 # 방문 표시
                    q.append([nx, ny])
    return [v_cnt, k_cnt]

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
# print(board)
v = 0
k = 0
for i in range(r):
    for j in range(c):
        if board[i][j] != '#' and visited[i][j] == 0:
            v_cnt, k_cnt = bfs(i, j)
            v += v_cnt
            k += k_cnt
print(k, v)