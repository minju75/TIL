t = int(input())
for tc in range(1, t+1):
    li = list(map(int,input().split()))
    avg = sum(li[1:])/li[0]
    # print(avg)
    cnt = 0
    a = 0.000
    for j in range(1, len(li)):
        if int(li[j]) > avg:
            cnt += 1
    print(str("%.3f" %round((cnt/li[0])*100, 3))+"%")
