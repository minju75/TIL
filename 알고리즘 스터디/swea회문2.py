def check(m):
    for i in range(100):
        for j in range(100-m+1):
            a = board[i][j:j+m]
            b = zboard[i][j:j+m]
            if a == a[::-1] or b == b[::-1]:
                return True
    return False

t = 10
for tc in range(1, 11):
    n = int(input())
    board = [input() for _ in range(100)]
    zboard = list(zip(*board))
    result = 0
    for z in range(100, 0, -1):
        if check(z):
            result = z
            break
    print("#%d %d" %(tc, result))