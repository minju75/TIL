def virus(v):
    global connect, queue, cnt
    visited[v] = 1
    for i in range(connect):
        if arr[i][0] == v and visited[arr[i][1]] == 0:
            queue.append(arr[i][1])
            cnt += 1
            visited[arr[i][1]] = 1
    while queue:
        a = queue.pop(0)
        for j in range(connect):
            if arr[j][0] == a and visited[arr[j][1]] == 0:
                queue.append(arr[j][1])
                cnt += 1
                visited[arr[j][1]] = 1
    return cnt


com = int(input())
connect = int(input())
arr = [list(map(int, input().split())) for _ in range(connect)]
queue = []
visited = [0] * (com+1)
cnt = 0
virus(1)
print(cnt)