n = int(input())
for i in range(n*2):
    for j in range(n):
        if (i+j)%2 == 0:
            print('*', end = '')

        elif (i+j)%2 == 1:
            print(' ', end = '')

    print('')