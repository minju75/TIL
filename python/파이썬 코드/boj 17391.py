n, m = map(int, input().split())
board = [list(map(int, input().split)) for _ in range(n)]
visited = [[0]*m for i in range(n)]
