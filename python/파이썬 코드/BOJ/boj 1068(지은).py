from collections import deque

N = int(input())
tree_arr = list(map(int, input().split()))
del_num = int(input())

child_list = [[] for _ in range(N)]
for i in range(N):
    if tree_arr[i] >= 0 and i != del_num:
        child_list[tree_arr[i]].append(i)

checked = [1]*N

deque1 = deque()
deque1.append(del_num)
while deque1:
    x = deque1.popleft()
    checked[x] = 0
    deque1.extend(child_list[x])
    child_list[x] = []

cnt = 0
for i in range(N):
    if checked[i] == 1 and child_list[i] == []:
        cnt += 1

print(cnt)