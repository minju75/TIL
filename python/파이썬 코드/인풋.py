import sys
sys.stdin = open('input.txt')

# board = [list(map(int, input().split())) for _ in range(2)]
# print(board)
#board = [list(input()) for _ in range(3)]
board = list(map(int, input().split('/')))
print(board)

