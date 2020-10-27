t = int(input())
for tc in range(1, t+1):
    n, m = input().split()
    jinsu_16 = int('0x'+m, 16)
    # print(jinsu_16)
    jinsu_2 = format(jinsu_16, 'b')
    #print(jinsu_2)
    if len(jinsu_2) < int(n)*4:
        jinsu_2 = '0'+jinsu_2

    print('#{} {}'.format(tc, jinsu_2))