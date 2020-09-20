def in_order(idx):
    global cnt
    if left[idx] != 0:
        cnt += 1
        in_order(left[idx])
        if right[idx] != 0:
            cnt += 1
            in_order(right[idx])


t = int(input())
for tc in range(1, t+1):
    e, n = map(int,input().split())
    node = list(map(int,input().split()))
    left = [0]*(e+2)
    right = [0]*(e+2)
    cnt = 1
    for i in range(e):
        parent, child = node[2*i], node[(2*i)+1]
        if left[parent] != 0:
            right[parent] = child
        else:
            left[parent] = child

    in_order(n)
    print('#%d %d' %(tc, cnt))