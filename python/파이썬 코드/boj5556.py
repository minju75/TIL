n = int(input())
k = int(input())
table = [[0]*n for _ in range(n)]
color = [1, 2, 3]
list = []
for m in range(n//2+1):
    list.append(m%3)

for q in range(n):
    for i in range(q, n-q):
        for j in range(q, n-q):
            table[i][j] = color[list[q]]

for i in range(k):
    a, b = map(int, input().split())
    print(table[a-1][b-1])