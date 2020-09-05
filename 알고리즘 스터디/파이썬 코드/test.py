p = "is"
t = "this is a book~!"
m = len(p)
n = len(t)

def bruteforce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < m and i < n :
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i+1
        j = j+1
    if j == m :
        return i-m
    else :
        retur -1
