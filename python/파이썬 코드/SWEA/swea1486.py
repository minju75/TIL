def dfs(idx, sum_v):
    global min_num
    if sum_v >= min_num:
        return

    if idx >= n:
        if sum_v >= b:
            min_num = sum_v
        return


t = int(input())
for tc in range(1, t+1):
    n, b = map(int,input().split())
    s = list(map(int,input().split()))
    selected = [0] * n
    min_num = 9607052
    dfs(0,0)
    print('#%d %d' %(tc, min_num-b))