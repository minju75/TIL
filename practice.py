num = []
for _ in range(9):
    num.append(int(input()))
 
max_num = num[0]
idx = 0
for i in range(9):
    if max_num < num[i]:
        idx = i
        max_num = num[i]

print(max_num, idx+1)