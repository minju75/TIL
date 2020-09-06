t = int(input())
for tc in range(1, t+1):
    li = list(input())
    cnt = 0
    total = 0
    for i in range(len(li)):
        if li[i] == 'O':
            cnt += 1
            total += cnt
        if li[i] == 'X':
            cnt = 0
    print(total)
