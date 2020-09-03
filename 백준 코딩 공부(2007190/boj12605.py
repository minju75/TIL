def findG(S):
    queue = list()
    queue.append((S, 0))
    visited = [0] * (V+1)
    visited[S] = 1
    while queue:
        cn, length = queue.pop(0)
        for i in range(V+1):
            if line_li[cn][i] == 1 and not visited[i]:
                if i == G:
                    return length+1
                queue.append((i, length+1))
                visited[cn] = 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    input_box = [list(map(int, input().split())) for _ in range(E)]
    line_li = [[0]*(V+1) for _ in range(V+1)]
    S, G = map(int, input().split())

    while input_box:
        a, b = input_box.pop(0)
        line_li[a][b] = line_li[b][a] = 1

    result = findG(S)
    print('#{} {}'.format(tc, result))