def dfs(idx,clock,dir):
    if idx < 0 or idx >= 4:
        return
    if dir == 3:
        dfs(idx + 1, -clock, 2) #오른쪽 탐색
        dfs(idx - 1, -clock, 1) # 왼쪽 탐색
        roll(idx,clock) #회전
    elif dir == 1:  #왼쪽 탐색중 이었다면,
        if mag[idx][2] != mag[idx+1][6]:
            dfs(idx-1,-clock,dir)
            roll(idx,clock)
    elif dir == 2:  #오른쪽 탐색중이었다면,
        if mag[idx][6] != mag[idx-1][2]:
            dfs(idx+1,-clock,dir)
            roll(idx, clock)

def roll(idx,clock):
    #반시계이면 제일 앞쪽꺼 떼서 뒤로 갖다 붙이면됨
    if clock == -1:
        tmp = mag[idx].pop(0)
        mag[idx].append(tmp)
    elif clock == 1:
        #시계이면 제일 뒤쪽꺼 떼서 맨앞에 갖다 붙이면 됨
        tmp = mag[idx].pop()
        mag[idx].insert(0,tmp)


T = int(input())
for tc in range(1,T+1):
    K = int(input())
    mag = [list(map(int,input().split())) for _ in range(4)]
    for i in range(K):
        idx, dir = map(int, input().split())
        dfs(idx-1,dir,3)
    result =0
    for i in range(4):
        if mag[i][0] == 1:
            result += (pow(2,i))
    print("#{} {}".format(tc,result))
#dir : 1왼쪽, 2 오른쪽, 3이면 시작
# clock 돌리는 방향 -1 반시계, 1이면 시계

