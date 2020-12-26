from collections import defaultdict, deque
import sys

def bfs(key):
    Q = deque([key])
    visited[key] = 1
    cnt = 0
    while Q:
        ql = len(Q)
        for i in range(ql):
            tmp = Q.popleft()
            if tmp == 1:
                break
            if dic.get(tmp):
                for i in dic[tmp]:
                    if visited[i] == 0:
                        Q.append(i)
                        visited[i] = 1
        if tmp == 1:
            break
        cnt += 1
    return cnt

n = int(input())
dic = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

del dic[1]
cnt = 0
for key, value in dic.items():
    if len(value) == 1:
        visited = [0] * (n+1)
        cnt += bfs(key)

if cnt % 2:
    print("Yes")
else:
    print("No")
