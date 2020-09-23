n, k = map(int, input().split())
num = list(map(int, input().split()))
num_sum = sum(num[0:k])
max_n = num_sum
i = 0
if k == 1:
    print(max(num))
else:
    while True:
        num_sum -= num[i]
        if i+k >= n:
            break

        num_sum += num[i+k]

        if num_sum > max_n:
            max_n = num_sum
        i += 1

    print(max_n)