for tc in range(1, 11):
    n = int(input())
    tree = [[0]*3 for _ in range(n+2)]
    # print(li)
    for i in range(n):
        li = input().split()
        if len(li) <= 2:
            tree[int(li[0])][2] = int(li[1])
        else :
            tree[int(li[0])][1] = int(li[3])
            tree[int(li[0])][2] = li[1]
            tree[int(li[0])][0] = int(li[2])
    print(tree)
    for q in range(n, 0, -1):
        if tree[q][2] == '*':
            tree[q][2] = tree[tree[q][0]][2] * tree[tree[q][1]][2]
        elif tree[q][2] == '-':
            tree[q][2] = tree[tree[q][0]][2] - tree[tree[q][1]][2]
        elif tree[q][2] == '/':
            tree[q][2] = tree[tree[q][0]][2] / tree[tree[q][1]][2]
        elif tree[q][2] == '+':
            tree[q][2] = tree[tree[q][0]][2] + tree[tree[q][1]][2]

    print('#%d %d' %(tc, tree[1][2]))
