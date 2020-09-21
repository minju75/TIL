t = 10
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2):
        minV = 987654321
        for j in range(5):
            if j != 2:
                if arr[i] - arr[i-2+j] < minV:
                    minV = arr[i] - arr[i-2+j]
        if minV > 0 :
            ans += minV

    print('#%d %d' %(tc+1, ans))