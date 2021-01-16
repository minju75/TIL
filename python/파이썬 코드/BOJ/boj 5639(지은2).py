import sys
sys.setrecursionlimit(10000)
# sys.stdin = open('input.txt', 'r')

def in_to_post(root_node, end_node):
    if root_node > end_node:
        return

    div = end_node+1
    for i in range(root_node+1, end_node+1):
        if arr[root_node] < arr[i]:
            div = i
            break

    in_to_post(root_node+1, div-1)
    in_to_post(div, end_node)
    print(arr[root_node])


arr = []

while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

if arr:
    in_to_post(0, len(arr)-1)