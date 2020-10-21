for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    sell = arr[n-1]
    ans = 0
    for i in range(n -2, -1, -1):
        if sell >= arr[i]:
            ans += (sell-arr[i])

        else :
            sell = arr[i]

    print('#%d %d' %(tc, ans))