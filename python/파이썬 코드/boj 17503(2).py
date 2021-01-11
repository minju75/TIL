import sys, heapq

N, M, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a,b])
arr.sort(key=lambda x:(x[1], x[0]))

beer = []
like_sum = 0
for i in range(K):
    heapq.heappush(beer, arr[i][0])
    like_sum += arr[i][0]
    level = arr[i][1]
    if len(beer)==N:
        if like_sum >= M:
            print(level)
            break
        else:
            if i == K-1:
                print(-1)
                break
            like_sum -= heapq.heappop(beer)