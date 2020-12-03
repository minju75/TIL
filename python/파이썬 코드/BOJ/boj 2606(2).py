def bfs(s):
    global board
    queue = [s] # 1 부터 append
    visited = [] # 감염된 컴퓨터를 담을 리스트
    while queue:
        ne = queue.pop(0)
        visited.append(ne)

        for i in range(c+1):
            if board[ne][i] == 1 and i not in visited and i not in queue: #감염이 되어있으면서 감염 컴퓨터 리스트에 없고 queue 안에 중복 되지도 않을 때
                queue.append(i) # queue에 append

    return len(visited)-1

c = int(input()) # 컴퓨터의 수
n = int(input()) # 연결된 노드의 수
board = [[0 for _ in range(c+1)] for _ in range(c+1)] # 연결 네트워크를 표시할 판때기

for _ in range(n):
    a, b = map(int, input().split())
    board[a][b] = 1 # 연결된 관계는 1로 표시
    board[b][a] = 1 # 연결된 관계는 1로 표시

print(bfs(1)) # 1번 컴퓨터가 바이러스에 걸린 걸로 가정하고 감염된 컴퓨터 수 파악