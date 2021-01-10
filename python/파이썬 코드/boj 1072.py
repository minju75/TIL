from math import floor
x, y = map(int, input().split())
e = floor(100 * y / x)
left = 0
right = 1000000000

if e >= 99 :
    print(-1)

else:
    while left <= right:
        mid = (left + right) // 2
        tx, ty = x + mid, y + mid
        if floor(100 * ty / tx) > e:
            right = mid - 1
        else:
            left = mid + 1

    print(right + 1)