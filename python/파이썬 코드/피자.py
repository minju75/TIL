t = int(input())
for tc in range(1, t+1):
    n,m = map(int,input().split())
    ch = list(map(int,input().split()))
    #queue = [0]*n
    pizza_num = [i for i in range(m)]
    queue = pizza_num[0:n]
    # print(visited)
    # for i in range(n):
    #     queue[i] = ch[i]
    # ch = ch[n:]
    while len(queue) != 1:
        if ch[queue[0]] != 1:
            ch[queue[0]] = ch[queue[0]]//2
            queue.append(queue.pop(0))
        else :
            queue.pop(0)
            if n != m:
                queue.append(pizza_num[n])
                n += 1
    print('#%d %d' %(tc, queue[0]+1))