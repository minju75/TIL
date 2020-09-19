def check(a):
    queue = []
    queue.append((a, 0))

    maxx = 0
    numm = 0

    while queue:
        # print(queue)
        # print(visited)
        s, cnt = queue.pop(0)

        if cnt > maxx:
            maxx = cnt
            numm = s
        elif cnt == maxx and s > numm:
            numm = s

        for i in range(101):

            if arr[s][i] and not visited[i]:
                # print(i)
                queue.append((i, cnt + 1))
                visited[i] = 1
    return numm


T = 10
for tc in range(1, T + 1):
    length, S = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[0] * 101 for _ in range(101)]
    # print(data)
    for i in range(0, length, 2):
        arr[data[i]][data[i + 1]] = 1

    visited = [0] * 101
    num = check(S)
    print(f'#{tc}', num)