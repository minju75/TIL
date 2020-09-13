import sys
R, C = map(int, input().split())
fence = [list(input()) for _ in range(R)]
#print(fence)
dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1]
result = 0
for i in range(R):
    for j in range(C):
        if fence[i][j] == 'S': # 양이라면 코드 계속 진행
            continue
        if fence[i][j] == 'W': # 늑대일 때
            for q in range(4): #델타로 방향 확인
                cr, cc = i+dr[q], j+dc[q]
                if cr == 0 or cr >= R or cc == 0 or cc <= C :
                    continue
                if fence[cr][cc] == 'S': #늑대의 옆에 양이 있으면 결과값을 '0'으로 주기
                    print(0)
                    break
        else : # '.'일 때 울타리를 d 로 변경경
            fence[i][j] = 'D '
            print(1, fence)
print(result)