def bfs(s):
    global board
    queue = [s] # 1 부터 append
    visited = [0] * (c+1) # 방문을 체크할 리스트
    cnt = 0 # 감염된 컴퓨터의 갯수를 셀 cnt
    while queue: # queue 가 빌 때까지
        next = queue.pop(0)
        visited[next] = 1 # 방문 체크

        for i in range(c+1): # 노트북의 수 만큼 for문 실행
            if board[next][i] == 1 and visited[i] == 0: #감염이 되어있으면서 방문 표시가 안 되어있을 때
                queue.append(i) # queue에 append
                visited[i] = 1 # 방문 체크
                cnt += 1 # cnt에 1 더해주기
    return cnt

c = int(input()) # 컴퓨터의 수
n = int(input()) # 연결된 노드의 수
board = [[0 for _ in range(c+1)] for _ in range(c+1)] # 연결 네트워크를 표시할 판때기

for _ in range(n):
    a, b = map(int, input().split())
    board[a][b] = 1 # 연결된 관계는 1로 표시
    board[b][a] = 1 # 연결된 관계는 1로 표시

print(bfs(1)) #1번 컴퓨터부터 확인해야하므로 bfs(1) 실행

