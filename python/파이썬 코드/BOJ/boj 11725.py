import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) # 최대재귀한도깊이 풀기

def find_p(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            find_p(i, tree, parent)

# def find_p(node_list, start, parent):
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         for i in node_list[node]:
#             if parent[i] == 0 :
#                 parent[i] = node
#     return parent

n = int(input())
tree = [[] for _ in range(n+1)] # 0을 제외해야 해서 n+1
parent = [0 for _ in range(n+1)] # 0을 제외해야 해서 n+1/ 부모 리스트를 확인할 리스트
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b) # 서로간의 연결관계 확인
    tree[b].append(a)
# print(tree)
find_p(1, tree, parent)
print(*parent[2:])
