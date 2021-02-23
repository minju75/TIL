import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 스태프의 수, 풍선의 개수
a = list(map(int, input().split())) # 스태프가 풍선 하나랄 만드는데 걸리는 시간

left = min(a) # 풍선 1개를 만드는데 걸리는 가장 작은 시간
right = min(a)*m # 풍선을 전부 만드는데 걸리는 최대 시간

# 이분탐색
while left+1 < right: # 탐색할 범위가 남아있는 동안 반복
    mid = (left + right) // 2 # 탐색 범위의 중간 위치
    cnt = 0
    for i in a:
        cnt += mid // i

    if cnt >= m:
        right = mid

    else:
        left = mid

print(right)