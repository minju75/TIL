def heappush(value):
    global heapcount
    heapcount += 1
    tree[heapcount] = value
    child = heapcount
    parent = child // 2
    while parent > 0 and tree[child] < tree[parent]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    li = list(map(int, input().split()))
    tree = [0] * (n+1)
    heapcount = 0
    for i in range(len(li)):
        heappush(li[i])
    cnt = 0
    while n > 1:
        cnt += tree[n//2]
        n = n//2
    print('#%d %d'%(tc,cnt))