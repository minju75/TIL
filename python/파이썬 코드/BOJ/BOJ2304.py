N = int(input()) # 기둥의 개수
stick = [] # L, H 를 담을 LIST
for i in range(N):
    L, H = map(int, input().split())
    stick.append([L, H])
stick.sort() # L의 위치 순서대로 리스트 정렬
# print(stick)
max_H = 0 # 최대 높이를 찾기 위한 설정
for i in range(N):
    if max_H < stick[i][1]:
        max_H = stick[i][1]
# print(max_H)
# print(max_idx)
a = stick[N-1][0]
height = [0] * (a+1)
for i in range(N):
    height[stick[i][0]] = stick[i][1]
max_idx = height.index(max(height))
# print(list)
for h in range(max_H, -1, -1): # 10, 9, 8, 7, 6, ...
    for right in range(max_idx, a+1): # 8~17
        if height[right] == h:
            for i in range(max_idx, right):
                if height[i] < h:
                    height[i] = h

    for left in range(0, max_idx): # 8~17
        if height[left] == h:
            for i in range(left, max_idx):
                if height[i] < h:
                    height[i] = h

print(sum(height))


