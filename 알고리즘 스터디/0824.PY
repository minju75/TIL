for tc in range(10):
    tc = int(input())
    n = 100
    a, z = [], ['' for i in range(100)]
    result = 1
    for i in range(n): # 가로줄
        b = input()
        a.append(b)
        # 세로줄
        for j in range(n):
            z[j] += b[j]
        
    for i in range(n):
        for m in range(n) :
            for k in range(n-m):
                if a[i][k:m+k+1] == a[i][m+k]+a[i][k:m+k][::-1]:
                    if m+1 > result:
                        result = m+1
                if z[i][k:m+k+1] == z[i][m+k]+z[i][k:m+k][::-1]:
                    if m+1 > result:
                        result = m+1
    print("#%d %d" %(tc, result))