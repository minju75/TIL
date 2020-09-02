for tc in range(1, 11):
    n = int(input())
    dump = list(map(int,input().split()))
    while n :
        dump[dump.index(max(dump))] -= 1
        dump[dump.index(min(dump))] += 1
        n -= 1

    print('#%d %d' %(tc, (max(dump)-min(dump))))