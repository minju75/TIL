def tree(v):
    global cnt, cnt_sum
    if visited == 1:
        return

    cnt += 1

    for j in range(len(tree_list[v])):
        if tree_list[v][j] != 1 and visited[tree_list[v][j]] == 0:
            # tree_cnt[tree_list[v][j]] = cnt
            cnt_sum += cnt
            visited[tree_list[v][j]] = 1
            tree(tree_list[v][j])
            cnt -= 1
    return

N = int(sys.stdin.readline())
tree_list = [[0]] + [[] for _ in range(N)]
# tree_cnt = [0] * (N+1)
visited = [0] * (N+1)
visited[1] = 1
visited[0] = 1
cnt_sum = 0
for _ in range(N-1):
    n, m = map(int, sys.stdin.readline().split())
    tree_list[n].append(m)
    tree_list[m].append(n)
for i in range(len(tree_list[1])):
    cnt = 1
    # tree_cnt[tree_list[1][i]] = cnt
    cnt_sum += cnt
    visited[tree_list[1][i]] = 1
    if len(tree_list[tree_list[1][i]]) != 1:
        tree(tree_list[1][i])

if cnt_sum % 2 == 0:
    print('No')
else:
    print('Yes')