t = int(input()) # 테스트케이스의 갯수
for _ in range(1, t+1):
    n = int(input()) # 공장 가로 세로의 길이
    factory = [list(map(int, input().split())) for _ in range(n)]
    # print(factory)
    human = []
    tal = []
    for i in range(n):
        for j in range(n):
            if factory[i][j] == 1:
                human.append([i+1, j+1])
            elif factory[i][j] == 2:
                tal.append([i+1, j+1])
    # print(human)
    # print(tal)
    stack = []
    for i in range(len(human)):
        a = human[i][0] - tal[0][0]
        if a < 0:
            a = a * (-1)
        b = human[i][0] - tal[0][1]
        if b < 0:
            b = b * (-1)
        c = a + b
        a_2 = human[i][0] - tal[1][0]
        if a_2 < 0:
            a_2 = a_2 * (-1)
        b_2 = human[i][0] - tal[1][1]
        if b_2 < 0:
            b_2 = b_2 * (-1)
        c_2 = a_2 + b_2
        if c <= c_2:
            stack.append(c)
        else:
            stack.append(c_2)
    print(stack)
