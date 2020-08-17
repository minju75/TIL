t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = []
    b = []
    for x in range(2, n):
        if n % x == 0:
            result = (n//x)
            a.append(x)
            if (n//x) == 1:
                break
            for z in a:
                q = a.count(z)
                b.append(q)
    
    print('#%d %d' %(i, b))
