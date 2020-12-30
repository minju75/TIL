n = int(input())
parent = list(map(int, input().split())) # 각 노드의 부모들
delete_node = int(input()) # 삭제할 노드의 번호
tree = {} # 딕셔너리 형태의 tree 생성
for i in range(n):
    if i == delete_node or parent[i] == delete_node:
        continue
    if parent[i] in tree: # 트리 안에 있다면
        tree[parent[i]].append(i)
    else: # 없다면
        tree[parent[i]] = [i]

# print(tree)

# dfs 이용
cnt = 0
if -1 in tree:
    que = [-1]
else:
    que = []
# print(que)
while que:
    node = que.pop()
    if node not in tree:
        cnt += 1
    else:
        que += tree[node]
print(cnt)