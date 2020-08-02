#n = int(input())
n = 6
if n == 1:
    print('*')
elif n%2 == 0:
    print('*'*(n//2))
    #print(' ' + ('*'*(n//2)))
    print(' '+('*'*(n//2)))
    #' '.join(a)
    #print(a)
    
elif n%2 == 1:
    print('*'*(n//2))
    #print(' '+'*'*(n-(n//2)))
    print(' '+'*'*(n-(n//2)))
    #' '.join(b)
    #print(b)