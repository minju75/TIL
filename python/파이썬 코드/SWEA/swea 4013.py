t = int(input())
for tc in range(1, t+1):
    k = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(k):
        idx, dir = map(int, input().split())
        idx -= 1
        move = [(idx, dir)]

        mag = dir
        for z in range(idx + 1, 4):
            if gear[z][6] != gear[z-1][2]:
                mag *= -1
                move.append((z, mag))

            else:
                break

        mag = dir
        for z in range(idx -1, -1, -1):
            if gear[z][2] != gear[z+1][6]:
                mag *= -1
                move.append((z, mag))

            else:
                break

        for idx, dir in move:
            if dir == 1:
                gear[idx] = [gear[idx].pop()] + gear[idx]

            elif dir == -1:
                gear[idx].append(gear[idx].pop(0))

    result = 0
    for i in range(4):
        result += gear[i][0] * (2**i)

    print('#%d %d' %(tc, result))