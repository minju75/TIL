import sys
sys.stdin = open("4256_트리.txt", "r")


def real_tree(v):
    global pre_result, in_result
    left = []
    right = []
    root = pre_result[0]
    i = in_result.index(root)
    if len(pre_result) == 2:
        postorder.append(pre_result[1])
        postorder.append(root)

    else:
        left = in_result[0:i]
        right = in_result[i+1:]
        pre_left = pre_result[1:1+i]
        pre_right = pre_result[1+i:]
        if len(left) > 0:
            if len(left) == 1:
                postorder.append(left[0])
            else:
                pre_result = pre_left
                in_result = left
                real_tree(0)

        if len(right) == 1:
            postorder.append(right[0])
            postorder.append(root)
        elif len(right) == 0:
            postorder.append(root)
        else:
            pre_result = pre_right
            in_result = right
            real_tree(0)
            postorder.append(root)



T = int(input())
postorder = []
for tc in range(T):
    n = int(input())
    pre_result = list(map(int, input().split()))
    in_result = list(map(int, input().split()))
    postorder = []
    real_tree(0)
    print(*postorder)
