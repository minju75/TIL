# 노드의 합

def dfs(idx):
    if idx > n+1: return 0
    if tree[idx]: return tree[idx]
    left = idx * 2
    right = idx * 2 + 1
    tree[idx] = dfs(left) + dfs(right)
    return tree[idx]


t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())   # 별도 노드 개수, 리프 노드의 개수, 출력 노드 번호
    tree = [0 for _ in range(n+2)]        # 입력값
    for i in range(m):
        node, value = map(int, input().split())
        tree[node] = value

    result = dfs(l)
    print('#%d %d' %(tc, result))