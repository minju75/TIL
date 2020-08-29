t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    li = list(map(int, input().split()))
    r = []
    for i in range(n//2):
        a = max(li)
        r.append(a)
        li.remove(a)

        b = min(li)
        r.append(b)
        li.remove(b)

        continue
    r = ' '.join(map(str,r[0:10]))
    print('#%d' %tc, r)