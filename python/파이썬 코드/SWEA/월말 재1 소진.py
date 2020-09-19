#살아있는 나무 체크하기위한 함수 실행
def check(r,c):
    global cnt
    # 스택을 생성하여 첫 방문한 위치인덱스 저장
    stack = []
    stack.append((r,c))
    # 스택 있을 때만 반복문 실행
    while stack:
        #현재 위치 스택에서 꺼내서 방문체크
        cr,cc = stack.pop()
        visited[cr][cc] = 1
        #델타 순회 시작
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            #상하좌우 델타를 순회하면서, 정원 나무 위치의 인덱스가 N*M안에 있음 체크
            #현재 위치의 나무가 미래 이동 위치 나무보다 크거나 같을 때만 생존 가능
            if 0 <= nr < N and 0 <= nc < M and Board[cr][cc] >= Board[nr][nc]:
            #그럴 때마다 생존 가능성 1씩 증가
                Alive[cr][cc] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정원 배열 받기
    Board = [list(map(int, input().split())) for _ in range(N)]
    # 함수 실행시 방문 체크
    visited = [[0]*M for _ in range(N)]
    # 살아있는 나무 개수 체크
    Alive = [[0]*M for _ in range(N)]
    # 상하좌우 순회 델타
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    cnt = 0
    r = 0
    c = 0
    #정원을 순회하면서 방문하지 않은 곳부터 살아있는 나무 체크 시작하기
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                check(i,j)

    #Alive 순회하면서 생존 가능성이 3보다 작으면 (상하좌우 4개 중 2개 이상에서 햇빛을 받을 수 없기때문에) 나무 사망
    #사망하는 나무 개수 세기
    result_cnt = 0
    for i in range(len(Alive)):
        for j in range(len(Alive[i])):
            if Alive[i][j] < 3:
                result_cnt +=1
    print('#%d' %tc, result_cnt)