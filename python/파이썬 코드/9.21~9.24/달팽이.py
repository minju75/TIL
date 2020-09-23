def solve(arr):
    x, y = 0, 0
    nx, ny = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0 # 0:우, 1:하, 2:좌, 3:상
    num = 1

    for i in range(n*n):
        x, y = nx, ny
        arr[x][y] = num
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >=n or ny < 0 or ny >= n:
            dir = (dir+1 % 4)
            nx = x + dx[dir]
            ny = y + dy[dir]

        num += 1

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [[0] * N for _ in range(n)]

    solve(arr)