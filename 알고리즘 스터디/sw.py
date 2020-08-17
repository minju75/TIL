tc = int(input())
for i in range(1, tc + 1):
    n = int(input())
    z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = []
    for x in range(1, 1000000):
        b = list(str(n*x))
        y += b
        if len(set(y)) == 10 :
            print('#%d %d' %(i, x*n))
            break

