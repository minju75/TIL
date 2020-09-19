for tc in range(1, 11):
    n = int(input())
    cnt = 0
    ta = list(map(int, input().split()))
    for i in range(2, n - 2):
        if (ta[i] > ta[i - 2]) and (ta[i] > ta[i - 1]) and (ta[i] > ta[i + 1]) and (ta[i] > ta[i + 2]):
            cnt += ta[i] - max([ta[i - 1], ta[i - 2], ta[i + 1], ta[i + 2]])

    print('#%d %d' % (tc, cnt))