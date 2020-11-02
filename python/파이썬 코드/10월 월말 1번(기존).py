def hab(plus): # 주어진 행의 합을 구하기 위한 함수
    global board, stack
    global r, n, x, y
    for q in range(y - 1, y - 1 + k):  # 행
        for g in range(x - 1, x - 1 + k):  # 열
            board[q][g] = plus[q][g]
            if g > n or g < 0 or q > n or q < 0:  # 범위를 벗어나면 -1을 출력하고 종료
                return -1
    oi = [] # 주어진 행의 숫자들을 담을 리스트
    for j in range(x):
        oi.append(board[n][j]) # 주어진 행의 숫자들을 oi에 append 해준다.
        return sum(oi) # 함수의 반환값으로 oi 리스트의 합을 반환


def gak(a):
    global stack
    global c, k
    plus = [] # 회전 되어진 숫자들을 담을 리스트
    # 90도 회전일 때
    if c % 360 == 90:
        for a in range(k):
            for b in range(k-1, -1, -1):
                plus.append(stack[b][a])
                hab(plus) # 합을 구하기 위한 함수 실행
    plus = []
    # 180도 회전일 때
    if c % 360 == 180:
        for a in range(k-1, -1, -1):
            for b in range(k):
                plus.append(stack[a][b])
                hab(plus) # 합을 구하기 위한 함수 실행
    plus = []
    # 270도 회전일 때
    if c % 360 == 270:
        for a in range(k-1, -1, -1):
            for b in range(k-1, -1, -1):
                plus.append(stack[b][a])
                hab(plus) # 합을 구하기 위한 함수 실행

    # 회전의 변동이 없을 때
    if c % 360 == 0:
        stack = plus
        hab(plus) # 합을 구하기 위한 함수 실행

t = int(input())
for tc in range(1, t+1):
    n, c, x, y, k, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    stack_2 = []
    stack = []
    for q in range(y-1, y-1+k): # 행
        for g in range(x-1, x-1+k): #열
            stack_2.append(board[q][g])
            if g > n or g < 0 or q > n or q < 0: # 범위를 벗어나면 -1을 출력하고 종료
                print(-1)
                break
    for i in range(0, k*k, k):
        stack.append(stack_2[i:i+k])
        # print(stack)
    gak(c) # 주어진 각도에 맞춰서 회전을 하기 위해 함수 실행
    result = gak(c)
    print('#%d %d' %(tc, result))