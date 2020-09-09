for tc in range(1, 11):
    v, e = map(int,input().split())
    map = [[0]*(v+1) for _ in range(v+1)]
    visited = []
    node = [list(map(int,input().split()))]
    # n = int(len(node)/2)
    # for i in range(n):
    #     map[node[2*i]][node[2*i+1]] = 1
    # print(map)

