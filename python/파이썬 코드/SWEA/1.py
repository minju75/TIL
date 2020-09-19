t = int(input())
for tc in range(1, t+1):
    n, m, d = map(int, input().split())
    table = [[0] * n for _ in range(n)]
    a = n//2
    table[a][a] = m
    b = []
    for i in range(a+1):
        b.append(m + (d*i))
    # print(b)
    for x in range(1, a+1):
        for i in range(a-x, a+x+1):
            for j in range(a-x, a+x+1):
                if table[i][j] == 0:
                    table[i][j] = b[x]
    print('#%d' %tc, end=" ")

    q = []
    for i in range(n):
        q.append(sum(table[i]))
    print(*q)
