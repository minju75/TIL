t = int(input())
for _ in range(1, t+1):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    bae = [list(map(int, input().split())) for _ in range(n)]
    queue = []
# print(board)
    for i in range(n):
        for j in range(n):
            if bae[i][j] == 1:
                queue.append((i. j))
        print(queue)


# 2
# 7
# 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0
# 9
# 0 0 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 1
# 1 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0
# 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 1