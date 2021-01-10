import math
x, y = map(int, input().split()) # x : 게임횟수, y: 이긴게임
z = math.floor(100 * y / x)
left = 0
right = 1000000000

if z >= 99 : # z가 절대 변하지 않을 때(z가 99거나 100일 때)
    print(-1) # -1 을 출력

else: # z가 변할 수 있을 때
    while left <= right:
        mid = (left + right) // 2
        nx = x + mid
        ny = y + mid
        if math.floor(100 * ny / nx) > z:
            right = mid -1
        else:
            left = mid + 1
    print(right)