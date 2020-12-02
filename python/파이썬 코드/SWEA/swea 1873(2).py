tank = ['^', 'v', '<', '>']
dir_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dr = [-1, 1, 0, 0]
dc = [0, 0 , -1, 1]
def search_tank():
    for i in range(h):
        for j in range(w):
            if game[i][j] in tank:
                return i, j, tank.index(game[i][j])

for tc in range(1, int(input())+1):
    h, w = map(int, input().split()) # 높이와 너비
    game = [list(input()) for _ in range(h)] # 2차원 리스트

    n = int(input()) # 명령어의 개수
    cmd_list = list(input())

    # 1 탱크 위치 찾기
    r = c = dir = -1
    # for i in range(h):
    #     for j in range(w):
    #         if game[i][j] in tank:
    #             r = i
    #             c = j
    #             dir = tank.index(game[i][j])
    #             break
    #     if r != -1 :
    #         break
    r, c, dir = seach_tank()
    # 2 명령어 처리
    for cmd in cmd_list:

        # 2-1 폭탄 발사를 할 때
        if cmd == "S":
            nr = r+dr[dir]
            nc = c+dc[dir]
            while 0 <= nr < h and 0 <= nc < w:
                if nr < 0 or nr >= h or nc < 0 or nc >= w : break
                if game[nr][nc] == '#': break
                if game[nr][nc] == '*':
                    game[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]

        # 2-2 방향을 조종할 때
        else:
            dir = dir_dict[cmd]
            # 전차 방향 바꾸기
            game[r][c] = tank[dir]

            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < h and 0 <= nc < w and game[nr][nc]=='.':
                game[nr][nc] = tank[dir]
                game[r][c] = '.'
                r, c, = nr, nc #현재 탱크의 위치
    # 3 출력
    print('#{}'.format(tc), end="")
    for i in range(h):
        for j in range(w):
            print(game[i][j], end="")
        print()