n = int(input())
num = list(map(int,input().split()))
m = max(num)
# print(m)
for i in range(n):
    num[i] = num[i]/m*100
    avg = sum(num)/n
print("%.2f" %avg)