t = int(input())
delta = [(0,1), (1,0), (-1,0), (0, -1), (1,1), (-1,1), (-1,-1), (1,-1)]
for tc in range(1, t+1):
    n, m = map(int,input().split())
    ta = [([0] * (n+1)) for _ in range(n+1)]
    a = n//2
    ta[a][a] = ta[a+1][a+1] = 2
    ta[a][a+1] = ta[a+1][a] = 1
    for i in range(m):
        x, y, c = map(int,input().split())
        r = []
        for i in range(8):
            d_x, d_y = delta[i]
            n_x, n_y = x+d_x, y+d_y
            while True :
                if n_x < 0 or n_y < 0 or n_x > n-1 or n_y > n-1:
                    r = []
                    break
                if ta[n_x][n_y] == 0:
                    r = []
                    break
                if ta[n_x][n_y] == c:
                    break
                else :
                    r.append((n_x,n_y))
                n_x, n_y = (n_x)+(d_x), (n_y)+(d_y)
            for fx, fy in r:
                if c == 1:
                    ta[fx][fy] = 1
                else:
                    ta[fx][fy] = 2
        ta[x][y] = c
    white = 0
    black = 0
    for i in range(n):
         for j in range(n):
            if ta[i+1][j+1] == 1 :
                white += 1
            elif ta[i+1][j+1] == 2:
                black += 1

    print('#%d %d %d' %(tc, white, black))