import sys
input = sys.stdin.readline


# def check(r,c,num):
#     # r,c에 놓여진 퀸에 의해 영향받는 칸에 num을 더해주는 함수
#     for d in range(4):
#         nr = r
#         nc = c
#         while True:
#             nr += dr[d]
#             nc += dc[d]
#             if 0 > nr or 0 > nc or nr >= N or nc >= N: #범위를 벗어나면
#                 break # break
#             chess[nr][nc] += num # 체스판에 숫자 표시

def n_queen(r):
    global cnt
    if r >= N:
        cnt += 1
        return

    for i in range(N): # 퀸을 놓을 장소를 파악
        if visited_y[i] == 0 and visited_xy[r + i] == 0 and visited_yx[r - i] == 0: # 0으로 표시된 자리에 퀸을 둘 수 있다
            # 만약에 현재 칸에 퀸을 놓을 수 있으면, 퀸을 놓고
            # r,i에 퀸을 놓고, 그 퀸에 의해 영향 받는 칸에 표시(+1)
            # visited_x[r] += 1
            visited_y[i] = 1
            visited_xy[r + i] = 1
            visited_yx[r - i] = 1
            # 다음 행으로 진행
            n_queen(r+1)
            # r,i 에 놓인 퀸에 의해 표시되었던 칸을 되돌림(-1)
            visited_xy[r + i] = 0
            visited_yx[r - i] = 0
            # visited_x[r] -= 1
            visited_y[i] = 0
    return

N = int(input())
#보드에 놓인 퀸이 영향을 미치는 곳을 표시하기 위한 배열
chess = [[0] * N for _ in range(N)] # 체스판
# visited_x = [0] * N
visited_y = [0] * N
visited_xy = [0] * (2*N -1)
visited_yx = [0] * (2*N -1)
cnt = 0
dr = [-1, 1, 1, -1] # 8방향
dc = [1, 1, -1, -1] # 8방향
n_queen(0)
print(cnt)