t = int(input())
for tc in range(1, t+1):
    book = list(map(int,input().split()))
    book_a = list()
    for j in range(2):
        s = 1
        e = book[0]
        page = book[j+1]
        cnt = 0

        while s <= e:
            m = (s+e)//2
            if m == page:
                break
            elif m < page:
                s = m
                cnt += 1
            else:
                e = m
                cnt += 1

        book_a.append(cnt)

    if book_a[0] < book_a[1]:
        print('#%d %s' %(tc, 'A'))
    elif book_a[0] > book_a[1]:
        print('#%d %s' %(tc, 'B'))
    else :
        print('#%d %d' %(tc, 0))