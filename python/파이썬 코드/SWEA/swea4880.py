def game(s, e):
    if s == e :
        return s

    center = (s+e)//2
    a = game(s, center)
    b = game(center+1, e)
    a_v = card[a]
    b_v = card[b]
    if a_v == 1:
        if b_v == 2:
            return b
        else:
            return a

    if a_v == 2:
        if b_v == 3:
            return b
        else:
            return a

    if a_v == 3:
        if b_v == 1:
            return b
        else:
            return a



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = list(map(int, input().split()))
    result = game(0, n-1)
    print('#%d %d' %(tc, result+1))