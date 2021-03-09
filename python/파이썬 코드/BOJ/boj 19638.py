import heapq
import sys

n, h, t = map(int, sys.stdin.readline().split()) # 인구수, 키, 뿅망치 횟수 제한
tall = []
for _ in range(n):
    heapq.heappush(tall, -int(sys.stdin.readline()))
# print(tall)
cnt = 0

for i in range(t):
    tmp = -heapq.heappop(tall)
    if tmp < h:
        heapq.heappush(tall, -tmp)
        break
    a = tmp//2
    if a == 0:
        a = 1
        cnt -= 1
    cnt += 1
    heapq.heappush(tall, -a)
tmp = -(heapq.heappop(tall))
if tmp < h: # 결과 리스트 안의 숫자가 처음 거인의 수와 같다면
    print("YES")
    print(cnt)
else: # 아니라면
    print("NO")
    print(tmp)