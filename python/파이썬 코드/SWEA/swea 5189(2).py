def dfs(i):
    global min_num, num_hab


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    e_li = [list(map(int, input().split())) for _ in range(n)]
    visited =[0] * n
    min_num= 960705
    num_hab = 0
    dfs(0)
