t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    s = 0
    move = k
    while s < n:
        if s + move == n:
            break
        elif s + move in a:
            cnt += 1
            s += move
            move = k
        else :
            move -= 1
            if move == 0 :
                cnt = 0
                break
    print('#%d %d' %(tc, cnt))