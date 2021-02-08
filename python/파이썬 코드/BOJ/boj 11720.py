string_count = int(input())
string = list(input())
res = 0
for i in range(string_count):
    res += int(string[i])
print(res)