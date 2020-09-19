t = int(input())
for tc in range(1, t+1):
    n,m = map(int,input().split())
    ch = list(map(int,input().split()))
    queue = [0]*n
    list = [i for i in range(m)]
    # queue_2 = [i for i in range(m)]
    # print(visited)
    for i in range(n):
        queue[i] = ch[i]
    ch = ch[n:]
    for i in range(1000):
        a = queue[0]//2
        if queue.count(0) == n-1:
            break
       # if queue_2
        if ch and queue[0]//2 == 0:
            queue.pop(0)
            queue.append(ch.pop(0))
            # if len(ch) == 0:
            #     ch.append(float('inf'))
        else :
            queue.pop(0)
            queue.append(a)
    print(queue)

    # for i in range(n):
    #     if queue[i] == 1:
    #         result = i
    #print(result)

    # print('#%d %d' %(tc, n+result))

