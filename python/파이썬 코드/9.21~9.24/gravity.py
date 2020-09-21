arr = [7,4,2,0,0,7,0,6,0]

result = 0
maxHeight = 0
for i in range(len(arr)):
    # i번째 최대 낙차값은 len(arr) - (i+1)
    maxHeight = len(arr) - (i+1)
    for j in range(i+1, len(arr)):
        if arr[i] <= arr[j]:
            maxHeight -= 1

    # 최대값 구하기
    if result < maxHeight:
        result = maxHeight
print(result)