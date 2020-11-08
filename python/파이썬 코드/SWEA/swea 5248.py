def find_set(s):
    if s == board[s]:
        return s
    else:
        return find_set(board[s])


def union(s, e):
    board[find_set(e)] = find_set(s)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    board = [0 * (n + 1)]
    for i in range(1, n + 1):
        board.append(i)

    for i in range(0, len(num), 2):
        start = num[i]
        end = num[i+1]
        union(start, end)

    group = []
    for i in range(len(board)):
        group.append(find_set(i))

    print('#{} {}'.format(tc, len(set(group))-1))




    # print(board)