def rotation(li):
    global c, k
    ro_li = []
    if c % 360 == 90:
        for a in range(k):
            for b in range(k-1, -1, -1):
                ro_li.append(li[b][a])

    if c % 360 == 180:
        for a in range(k-1, -1, -1):
            for b in range(k):
                ro_li.append(li[a][b])

    if c % 360 == 270:
        for a in range(k-1, -1, -1):
            for b in range(k):
                ro_li.append(li[b][a])

    if c % 360 == 0:
        for a in range(k):
            for b in range(k):
                ro_li.append(li[a][b])

    return ro_li

t = int(input())
for tc in range(1, t+1):
    n, c, x, y, k, r = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(n)]
    # print(num)
    stack = []
    stack_2 = []
    ro_li2 = []
    ans = 0
    for q in range(y-1, y-1+k):
        for g in range(x-1, x-1+k):
            # print(q, g)
            if g >= n or g < 0 or q >= n or q < 0:  # 범위를 벗어나면 -1을 출력하고 종료
                print('#%d' %tc, -1)
                ans = -1
                break
            stack.append(num[q][g])
    if ans != -1:
        # print(stack)
        for i in range(0, k*k, k):
            stack_2.append(stack[i:i+k])

        result = rotation(stack_2)
        i=0
        for q in range(y-1, y-1+k):
            for g in range(x-1, x-1+k):
                num[q][g] = result[i]
                i += 1
        ap = []
        for j in range(n):
            ap.append(num[r-1][j])


        print('#%d %d' %(tc, sum(ap)))
        # print(num)
        # print(result)
        # print(stack_2)