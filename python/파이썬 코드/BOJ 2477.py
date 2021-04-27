k = int(input())
field = [list(map(int, input().split())) for _ in range(6)]
w = 0
w_idx = 0
h = 0
h_idx = 0
for i in range(len(field)):
    if field[i][0] == 1 or field[i][0] == 2:
        if w < field[i][1]:
            w = field[i][1]
            w_idx = i

    elif field[i][0] == 3 or field[i][0] == 4 :
        if h < field[i][1]:
            h = field[i][1]
            h_idx = i

s_w = abs(field[(w_idx-1)%6][1] - field[(w_idx+1)%6][1])
s_h = abs(field[(h_idx-1)%6][1] - field[(h_idx+1)%6][1])
ans = ((w*h) - (s_w * s_h)) * k
print(ans)