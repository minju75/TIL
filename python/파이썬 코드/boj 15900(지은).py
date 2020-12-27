import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
deque1 = deque()
checked = [0]*(N+1)
checked[1] = 1

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
    if a == 1:
        deque1.append((b,1))
        checked[b] = 1
    if b == 1:
        deque1.append((a,1))
        checked[a] = 1

cnt = 0
while deque1:
    x, c = deque1.popleft()
    l = len(deque1)
    for i in arr[x]:
        if checked[i] == 0:
            deque1.append((i, c+1))
            checked[i] = 1
    if l == len(deque1):
        cnt += c

if cnt % 2 == 1:
    print('Yes')
else:
    print('No')