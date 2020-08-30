n = input()
while n != '0':
    # n = list(map(str,input().split()))
    # if n == '0':
    #     break

    if n == n[::-1]:
        print('yes')

    else:
        print('no')
    n = input()