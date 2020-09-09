def check(num):
    temp = str(num)

    for i in range(1, len(temp)):
        if temp[i-1] > temp[i]:
            return -1
    return num

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_value = -1
    #모든 경우의 수 구하기
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            tmp = check(nums[i]*nums[j])

            if max_value <tmp :
                max_value = tmp

    print("#{} {}".format(tc, max_value))
