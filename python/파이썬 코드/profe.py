def backtrack(idx, sum_v):
    global min_sum
    if idx == n :
        # 모든 행에서 숫자 하나씩 선택한 상황
        # 최소합
        
        return

    for i in range(n):
        if not selected[i]:
            selected[i] = 1
            tmp = sum_v + arr[idx][i]
            if tmp < min_sum:
                backtrack(idx+1, tmp)
            selected[i] = 0




t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    selected = [0]*n
    min_sum = 100
    backtrack(0,0)
    print('#%d %d' %(tc, ))
