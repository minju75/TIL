t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    m = list(map(int, input()))
    # print(m)
    a = m.count(m[0])
    b = m[0]
    for i in range(len(m)):
        if a < m.count(m[i]):
            a = m.count(m[i])
            b = m[i]

        elif m.count(m[i]) == a and b < m[i]:
            b = m[i]

        else:
            max_num = m[0]

    print('#%d %d %d' % (tc, b, a))