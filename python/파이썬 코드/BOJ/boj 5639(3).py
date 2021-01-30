import sys
sys.setrecursionlimit(100000)

def postorder(s_node, e_node):
    if s_node > e_node:
        return

    mid = 0

    for i in range(s_node+1, e_node+1):
        if arr[s_node] < arr[i]:
            mid = i
            break

    postorder(s_node+1, mid-1)
    postorder(mid, e_node)
    print(arr[s_node])



arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

if arr:
    postorder(0, len(arr)-1)
