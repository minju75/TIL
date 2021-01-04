t = int(input())
for _ in range(1, t+1):
    arr = list(map(str, input().split()))
    word = list(arr[1])
# print(word)
    pp = ''
    for i in word :
        pp += i * int(arr[0])

    print(pp)