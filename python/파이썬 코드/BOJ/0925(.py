t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    signal = list(map(int, input().split()))
    key = list(map(int, input().split()))
    signal_2 = []
    for i in range(n):
        signal_2.append(signal[i])
    # print(list)
    # print(signal)
    # print(key)
    stack = []
    x = 0
    for j in range(n):
        if key[x] != signal[j]:
            signal_2.pop(0)
        else:
            signal_2.pop(0)
            stack.append(signal[j])
            x += 1
            if x == k:
                break
    # print(stack)
    if stack == key:
        result = 1
    else:
        result = 0

    print('#%d %d' %(tc, result))
