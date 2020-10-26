r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(c)]
arr = [[0]*(r+2) for _ in range(c+2)]
# print(arr)