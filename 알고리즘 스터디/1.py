for i in range(1):
    n = int(input())
    m = 100
    a  = [list(map(int,input().split())) for _ in range(m)]
    y = a[n-1].index(2)
    cnt = 0
    mov = 0
    while (n-1) > 0:
        if (move==0 or move==1) and y>0 and a[n-1][y-1]:
            y -= 1
            move = 1
        elif (move==0 or move==2) and y<n-1 and a[n-1][y-1]:
            y += 1
            move = 2
        else : 
            (n-1) -= 1
            move = 0
    print('#%d %d' %(i, y))