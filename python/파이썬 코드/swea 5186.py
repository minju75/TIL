t = int(input())
for tc in range(1, t+1):
    n = float(input())
    li = []
    sosu = ['9', '9']
    while (sosu[1] != '0' and len(li)<13):
        n = n*2
        sosu = str(n).split('.')
        li.append(sosu[0])
        n = float('0.'+sosu[1])

    if len(li) > 12:
        result = 'overflow'

    else:
        result = ''.join(li)

    print('#{} {}'.format(tc, result))