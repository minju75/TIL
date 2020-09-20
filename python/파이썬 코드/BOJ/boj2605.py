# N = int(input())
# list = list(map(int, input().split()))
# board = [0]*N
# for i in range(N):
#     board[list[i]] = i
#     if board[list[i]] != 0:
#         board[list[i]+1] = i-1
# print(board)


# n = int(input())
# list = list(map(int, input().split()))
# index = []
# for i in range(1, n+1):
#     index[i-list[i-1]] = i
    # index.append(i)
    # index = index[:i-1-list[i-1]] + [index[i-1]] + index[i-1-list[i-1]:i-1]
# print(index)


n = int(input())
list = list(map(int, input().split()))
index = []
for i in range(1, n+1):
    index[i-list[i-1]] = i
print(index)