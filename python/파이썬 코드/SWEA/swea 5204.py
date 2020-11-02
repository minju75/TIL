def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    global cnt
    result = []
    while len(left_arr) > 0 or len(right_arr) > 0:
        if len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] <= right_arr[0]:
                result.append(left_arr.pop(0))
            else:
                result.append(right_arr.pop(0))
        elif len(left_arr) > 0:
            result.append(left_arr.pop(0))
        elif len(right_arr) > 0:
            result.append(right_arr.pop(0))

    if left_arr[-1] > right_arr[-1]:
        cnt += 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#%d %d %d' %(tc, arr[n//2], cnt))