dr = [0,0,0,-1,1]
dc = [0,-1,1,0,0]
def shoot(r, c) :
    global map_2
    global h, w
    if map_2[r][c] == '*':
        map_2[r][c] = '.'
    elif map_2[r][c] == '.' or map_2[r][c] == '-':
        if 0 <= r + dr[dir] < h and 0 <= c + dc[dir] < w:
            shoot(r+dr[dir], c+dc[dir])

def play(r, c, start):
    global move, map_2
    global dir
    for i in move:
        if i == 'S':
            shoot(r + dr[dir], c + dc[dir])

        elif i == 'U':
            dir = 3
            if map_2[r-1][c] == '.':
                map_2[r][c] = '.'
                map_2[r-1][c] = '^'
                r -= 1
            else:
                map_2[r][c] = '^'

        elif i == 'D':
            dir = 4
            if map_2[r+1][c] == '.':
                map_2[r][c] = '.'
                map_2[r+1][c] ='v'
                r += 1
            else:
                map_2[r][c] = 'v'

        elif i == 'R':
            dir = 2
            if map_2[r][c+1] == '.':
                map_2[r][c] = '.'
                map_2[r][c+1] = '>'
                c += 1
            else :
                map_2[r][c] = '>'

        elif i == 'L':
            dir = 1
            if map_2[r][c-1] == '.':
                map_2[r][c] = '.'
                map_2[r][c-1] = '<'
                c -= 1
            else:
                map_2[r][c] = '<'



t = int(input())
for tc in range(1, t+1):
    h, w = map(int, input().split())
    map_2 = [list(str(input())) for _ in range(h)]
    n = int(input())
    move = list(str(input()))
# print(map)
# print(move)
    for a in range(h):
        for b in range(w):
            if map_2[a][b] == '>':
                dir = 1
                start = map_2[a][b]
                r, c = a, b

            if map_2[a][b] == '<':
                dir = 2
                start = map_2[a][b]
                r, c = a, b

            if map_2[a][b] == '^':
                dir = 3
                start = map_2[a][b]
                r, c = a, b

            if map_2[a][b] == 'v':
                dir = 4
                start = map_2[a][b]
                r, c = a, b
    play(r, c, start)
    # print(start)

    print(f'#{tc}', end=' ')
    for i in range(h):
        for j in range(w):
            print(map_2[i][j], end='')
        print()

