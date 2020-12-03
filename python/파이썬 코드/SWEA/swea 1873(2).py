tank = ['^', 'v', '<', '>']
dir_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search_tank():
    for i in range(H):
        for j in range(W):
            if game[i][j] in tank:
                return i, j, tank.index(game[i][j])


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())  # 높이와 너비
    game = [list(input()) for _ in range(H)]  # 2차원리스트 입력
    N = int(input())  # 명령어의 개수
    cmd_list = list(input())

    # 1. 탱크 위치를 찾기
    r = c = dir = -1
    # for i in range(H):
    #     for j in range(W):
    #         if game[i][j] in tank:
    #             r = i
    #             c = j
    #             dir = tank.index(game[i][j])
    #             break
    #     if r != -1:
    #         break
    r, c, dir = search_tank()
    # 2. 명령어 처리
    for cmd in cmd_list:
        # 2-1. 포탄발사를 할 때
        if cmd == 'S':
            nr = r + dr[dir]
            nc = c + dc[dir]
            while 0 <= nr < H and 0 <= nc < W:
                # 맵 밖을 벗어난 경우
                # if nr < 0 or nr >= H or nc < 0 or nc >= W:
                #     break
                if game[nr][nc] == '#': break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]

        # 2-2. 방향을 조종할 때
        else:
            dir = dir_dict[cmd]
            # 전차방향 바꾸기
            game[r][c] = tank[dir]
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < H and 0 <= nc < W and game[nr][nc] == '.':
                game[nr][nc] = tank[dir]
                game[r][c] = '.'
                r, c = nr, nc  # r,c 현재 탱크의 위치
    # 3. 출력
    print("#{}".format(tc), end=" ")
    for i in range(H):
        print(''.join(game[i]))