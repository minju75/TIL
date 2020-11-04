def dfs(board, V):
    visited = []
    stack = [V]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(board[node], reverse=True))
    return visited

def bfs(board, V):
    visited = []
    queue = [V]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(board[node]))
    return visited

N, M, V = map(int, input().split())

board = [set([]) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a].add(b)
    board[b].add(a)
# print(board)
print(*dfs(board, V))
print(*bfs(board, V))
