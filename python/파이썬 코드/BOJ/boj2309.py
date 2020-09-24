num = [int(input()) for _ in range(9)]
num.sort()
sum_n = sum(num)
for i in range(0, 8):
    for j in range(i+1, 9):
        if sum_n - (num[i]+num[j]) == 100:
            num.pop(j)
            num.pop(i)
            break
    if len(num) == 7:
        break

for i in num:
    print(i)
