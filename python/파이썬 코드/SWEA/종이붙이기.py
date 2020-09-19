def get(n):
    if n == 10 :
        return 1
    elif n == 20:
        return 3
    elif (n//10)%2 == 0 : 
        return ((get(n-20)*4)-1)
    elif (n//10)%2 != 0 :
        return ((get(n-20)*4)+1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    print('#%d %d' %(tc, get(n)))