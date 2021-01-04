import sys
input = sys.stdin.readline

def Postorder(preorder, inorder):
    if len(preorder) == 0: # len 한 값이 0 일때
        return # return

    root = preorder[0] # 전위 순회 한 리스트의 0번째 값이 무조건 root
    mid = inorder.index(root) # 중위 순회 한 리스트에서 root의 인덱스 번호

    Postorder(preorder[1:mid + 1], inorder[0:mid]) # 왼
    Postorder(preorder[mid + 1:len(preorder)], inorder[mid + 1:len(inorder)]) # 오

    print(root, end=" ")


t = int(input())
for _ in range(1, t+1):
    N = int(input())


    preorder = list(map(int, input().split())) # 전위 순회 입력 받기
    inorder = list(map(int, input().split())) # 중위 순회 입력 받기

    Postorder(preorder, inorder)
    print()