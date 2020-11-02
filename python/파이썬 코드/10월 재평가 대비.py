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
    for q in range(y-1, y-1+k):
        for g in range(x-1, x-1+k):
            stack.append(num[q][g])
    # print(stack)
    for i in range(0, k*k, k):
        stack_2.append(stack[i:i+k])
        rotation(stack_2)
    # print(stack_2)
