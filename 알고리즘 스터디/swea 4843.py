t = int(input())
for tc in range(1, t+1):
    n = int(input())
    li = list(map(int,input().split()))
    r = []
    while len(li) > 0 :
        a = max(li)
        li.remove(a)
        r.append(a)

        b = min(li)
        li.remove(b)
        r.append(b)
    r = ' '.join(map(str,r[0:10]))

    print('#%d' %(tc), r)