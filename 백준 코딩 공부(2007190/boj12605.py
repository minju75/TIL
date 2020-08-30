t = int(input())
b = ' '
for tc in range(1, t+1):
    a = list(map(str,input().split()))
    print('Case'' ''#%d' ':' %(tc),end='')
    for i in range(len(a)):
        c = a.pop()
        print(' 'c,end=' ')