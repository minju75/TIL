for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    li = [list(input()) for _ in range(N)]

    row = 0
    for i in range(N):
        if '1' in li[i]:
           row = i
           break

    col = 0
    for i in range(M-1,-1,-1):
        if li[row][i] == '1':
            col = i
            break

    # print(row, col)
    arr = []
    for i in range(8):
        arr.append(li[row][col-55+(i*7):col-55+((i+1)*7)])
    # print(arr)
    arrr =[]
    for i in arr:
        if i == ['0','0','0','1','1','0','1']:
            arrr.append(0)
        elif i == ['0','0','1','1','0','0','1']:
            arrr.append(1)
        elif i == ['0','0','1','0','0','1','1']:
            arrr.append(2)
        elif i == ['0','1','1','1','1','0','1']:
            arrr.append(3)
        elif i == ['0','1','0','0','0','1','1']:
            arrr.append(4)
        elif i == ['0','1','1','0','0','0','1']:
            arrr.append(5)
        elif i == ['0','1','0','1','1','1','1']:
            arrr.append(6)
        elif i == ['0','1','1','1','0','1','1']:
            arrr.append(7)
        elif i == ['0','1','1','0','1','1','1']:
            arrr.append(8)
        elif i == ['0','0','0','1','0','1','1']:
            arrr.append(9)
    # print(arrr)
    summ = 0
    for i in [0,2,4,6]:
        summ += arrr[i]*3
    for i in [1,3,5,7]:
        summ += arrr[i]
    # print(summ)
    if summ % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc}',sum(arrr))