# subtree
# 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내기

def in_order(idx):
    global cnt
    if left[idx] != 0:
        cnt += 1
        in_order(left[idx])
        if right[idx] != 0:
            cnt += 1
            in_order(right[idx])

t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split()) # 간선의 갯수
    node = list(map(int, input().split())) # e 개의 부모 자식 노드 번호 쌍
    left = [0]*(e+2)
    right = [0]*(e+2)
    cnt = 1
    for i in range(e):
        parent = node[2*i]
        child = node[(2*i)+1]

        if left[parent] != 0:
            right[parent] = child

        else:
            left[parent] = child

    in_order(n)
    print('#%d %d' %(tc, cnt))

    # print(left)
    # print(right)