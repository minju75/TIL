n = int(input())
h = int(input())
board = [[0]*n for _ in range(n)]
k = 0
m = 1
while k < n//2+1:
    for i in range(0+k, n-k):
        for j in range(0+k, n-k):
            board[i][j] = m
    k += 1
    if m == 3:
        m = 1
    else:
        m += 1

for q in range(h):
    a, b = map(int, input().split())
    num = board[a-1][b-1]
    print(num)