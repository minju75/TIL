N = int(input())
#보드에 놓인 퀸이 영향을 미치는 곳을 표시하기 위한 배열
check = [[0] * N for _ in range(N)]
cnt = 0
def marking(r,c,num):
    # r,c에 놓여진 퀸에 의해 영향받는 칸에 num을 더해주는 함수
    # num은 1 또는 -1
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            if 0 > nr or 0 > nc or nr >= N or nc >= N:
                break
            check[nr][nc] += num

def n_queen(r):
    global cnt
    if r >= N:
        cnt += 1
        return
    for i in range(N):
        if check[r][i] == 0:

            marking(r,i,1)
            n_queen(r+1)
            marking(r, i, -1)
    return

n_queen(0)
print(cnt)