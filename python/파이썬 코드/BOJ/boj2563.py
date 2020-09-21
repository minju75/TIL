n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    a, b = map(int, input().split())
    for r in range(a, a+10):
        for c in range(b, b+10):
            paper[r][c] = 1
a = 0
for row in paper:
    a += row.count(1)

print(a)