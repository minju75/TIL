n = 6
a = n*(n+1)//2
table = [[0]*i for i in range(1,1+n)]
move = [(1,1), (0,-1), (-1,0)] # 대, 좌, 상
r, c = 0, 0
num = 1
cnt = 1
table[r][c] = num
num += 1

while cnt < a:
    for dr, dc in move:
        while 0 <= r + dr < n and 0 <= c + dc < n and table[r + dr][c + dc] == 0:
            table[r+dr][c+dc] = num
            cnt += 1
            num += 1
            r += dr
            c += dc

for r in table:
    print(*r)