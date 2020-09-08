t = int(input())
for tc in range(1, t+1):
    v, e = map(int,input().split())
    ta = [([0]*(v+1)) for _ in range(v+1)]
    n = [list(map(int,input().split())) for _ in range(e)]
    for j in n:
        ta[j[0]][j[1]] = 1
    q, e = map(int,input().split())
    m = []
    while True :
        if 1 in ta[q]: 
            k = ta[q].index(1)
            ta[q][k] = 0
            m.append(q)
            q = k
            if k == e : 
                result = 1
                break
        
        else:
            if m == []:
                result = 0
                break
            else : 
                q = m.pop(0)

    print('#%d %d' %(tc, result))



