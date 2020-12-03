N = int(input())
tree = {}
for i in range(N-1):
    a,b = map(int,input().split())
    if tree.get(a):
        tree[a].append(b)
    else:
        tree[a] = [b]

visited = [0]*(N+1)
order = list(map(int,input().split()))
stack = [1]
i = 1
while stack and i<len(order):
    if tree.get(stack[-1]) and order[i] in tree[stack[-1]] and visited[order[i]]!=1:
        stack.append(order[i])
        i += 1
        visited[order[i]]=1
    else:
        stack.pop()

if not stack and i != len(order):
    print(0)
else:
    print(1)