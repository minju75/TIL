def dfs(c, val):
    global people
    if c >= N and people < val:
        people = val
        return

    for i in range(c, N):
        dfs(i+2, val+conference_li[i][2])


N = int(input())
conference_li = [tuple(map(int, input().split())) for _ in range(N)]
conference_li.sort()
people = 0
dfs(0, 0)

print(people)