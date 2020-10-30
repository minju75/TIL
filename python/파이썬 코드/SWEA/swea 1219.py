for tc in range(1, 11):
    t, n = map(int, input().split())
    node = list(map(int, input().split()))
    node_li = {x:[] for x in range(100)}
    for i in range(0, n*2, 2):
        start = node[i]
        end = node[i+1]
        node_li[start].append(end)

    stack = [0]
    visit = [0] * (100)
    visit[0] = 1
    result = 0
    while stack:
        current = stack.pop()
        for i in node_li[current]:
            if i == 99:
                result = 1
                break
            elif visit[i] == 0:
                stack.append(i)
                visit[i] = 1


    print('#%d %d' %(t, result))