T = int(input())
for tc in range(1,T+1):
    case_num, n = map(str,input().split())
    n = int(n)
    cases = list(map(str, input().split()))
     
    sort_list = [0]*10
    chr_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT','NIN']
    for i in range(n):
        if cases[i] == 'ZRO':
            sort_list[0] += 1
        elif cases[i] == 'ONE':    
            sort_list[1] += 1
        elif cases[i] == 'TWO':
            sort_list[2] += 1
        elif cases[i] == 'THR':
            sort_list[3] += 1
        elif cases[i] == 'FOR':
            sort_list[4] += 1
        elif cases[i] == 'FIV':
            sort_list[5] += 1
        elif cases[i] == 'SIX':
            sort_list[6] += 1
        elif cases[i] == 'SVN':
            sort_list[7] += 1
        elif cases[i] == 'EGT':
            sort_list[8] += 1
        elif cases[i] == 'NIN':
            sort_list[9] += 1
    print(case_num)
    for i in range(10):
        print((chr_list[i]+" ") * sort_list[i],end="")             