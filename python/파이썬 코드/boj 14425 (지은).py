import sys

N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline() for _ in range(N)]

cnt = 0
for _ in range(M):
    if sys.stdin.readline() in arr:
        cnt += 1

print(cnt)