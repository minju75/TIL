import copy
t = 10
for tc in range(1, t+1):
    n = int(input())
    m = 100
    a  = [list(map(int,input().split())) for _ in range(m)]
    a.append([])
    for i in range(m):
        a[i].append(0)

    s = []
    for i in range(m):
        if ladder[0][i] == 1:
            s.append(i)

    x = 0
    y = 0
    count = 0
    result = 1000
    result2 = 100
    ladder_2 = []
    for i in s:
        y = i
        x = 0
        count = 0
        ladder_2 = copy.deepcopy(ladder)
        while x < 100:
            if ladder_2[x][y+1] == 1:
                ladder_2[x][y+1] = 0
                y += 1
                count += 1

            elif ladder_2[x][y-1] == 1:
                ladder_2[x][y-1] = 0
                y -= 1
                count += 1

            elif ladder_2[x+1][y] == 1:
                ladder_2[x+1][y] = 0
                x += 1
                count += 1

            if x == 99:
                if result > count:
                    result = count
                    result2 = i
                elif result == count:
                    if result2 < i :
                        result2 == i
                break
	
    print('#%d %d' %(tc, result2))