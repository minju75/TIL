n = int(input())
li = [list(map(int, input().split())) for _ in range(n-1)]
ans = list(map(int, input().split()))
left = [0]*(n+1)
right = [0]*(n+1)
for i in range(n-1):
    if left[li[i][0]] == 0:
        left[li[i][0]] = li[i][1]
    else:

