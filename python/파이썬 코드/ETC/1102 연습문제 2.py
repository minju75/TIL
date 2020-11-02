li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li_size = len(li)
# print(li_size)
li_pow = []
for i in range(2 ** li_size):
    flag = bin(i)[2:].zfill(li_size)
    subset = [li[j] for j in range(li_size) if flag[j] == '1']
    li_pow.append(subset)

# print(li_pow)
for q in range(len(li_pow)):
    if sum(li_pow[q]) == 10:
        print(li_pow[q])