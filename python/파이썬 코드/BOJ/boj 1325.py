import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [[0]*(n+1) for _ in range(n+1)]
computers = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    board[b][a] = 1  # b 를 해킹하면 a도 해킹할 수 있다.
    computers[b] += 1 # b에 연결된 신뢰 컴퓨터의 수

    for i in range(n+1):
        if board[i][b]== 1: # b가 신뢰하는 컴퓨터인가?
            computers[i] += computers[b]

top = max(computers)
for i in range(len(computers)):
    if top <= computers[i]:
        print(i, end=' ')