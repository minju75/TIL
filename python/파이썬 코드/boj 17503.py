import heapq
import sys

n, m, k = map(int, sys.stdin.readline().split()) # n : 기간, m : 채워야하는 선호도의 합, k : 마실 수 있는 맥주 종류의 수
beer = [] # 선호도와 도수 레벨을 입력받을 리스트
pre = [] # 맥주의 선호도만 입력받을 리스트

for _ in range(k):
    v, c = map(int, sys.stdin.readline().split()) # v : 선호도, c : 도수 레벨
    beer.append((v, c))
# print(beer)
check = False # 조건이 맞는지 틀렸는지 확인해줄 것(조건에 해당하지 못하면 '-1'을 출력해야하므로!)
p_le = 0 # 맥주의 선호도를 더해줄 것
alc = 0 # 도수를 더해줄 것(간)
for i in range(k):
    heapq.heappush(pre, beer[i][0]) # 선호도 입력
    p_le += beer[i][0]
    alc += beer[i][1]
    print(pre)
    if len(pre) == n:
        if p_le >= m: # 맥주의 선호도가 채워야하는 선호도의 합보다 크거나 같으면
            check = True
            print(alc)
            break
        else: # 채워야하는 선호도의 합보다 작다면
            p_le -= heapq.heappop(pre) # 선호도가 작은 것 부터 빼주기
if not check: # 체크가 바뀌지 않았을 때 => 아무리 레벨을 올려도 조건을 만족시키지 못한다면
    print(-1)

