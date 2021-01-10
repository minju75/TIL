import heapq

n, h, t = map(int, input().split()) # 인구수, 키, 뿅망치 횟수 제한
tall = []
result = []
for _ in range(n):
    heapq.heappush(tall, -int(input()))
# print(tall)
cnt = 0
check = False
for i in range(t):
    tmp = -heapq.heappop(tall)
    if tmp < h:
        check = True
        break
    a = tmp//2
    if a == 0:
        a = 1
    cnt += 1
    if a == 1: # 거인의 키가 1이라면
        heapq.heappush(tall, -1)
        continue
    if a < h: # 거인의 키가 센티보다 작다면
        heapq.heappush(tall, -a)
    else: # 작아질 때까지!
        heapq.heappush(tall, -a)
tmp = -(heapq.heappop(tall))
if check or tmp < h: # 결과 리스트 안의 숫자가 처음 거인의 수와 같다면
    print("YES")
    print(cnt)
else: # 아니라면
    print("NO")
    print(tmp)