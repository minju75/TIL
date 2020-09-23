t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxv = 0

    for x in range(n-m+1):
        for y in range(n-m+1):
            # 파리채의 크기
            sumv = 0
            for i in range(m):
                for j in range(m):
                    sum += arr[x+i][y+j]
                if maxv < sumv:
                    maxv = sumv

    print(max)
