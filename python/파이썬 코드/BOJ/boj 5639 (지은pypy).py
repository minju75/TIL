import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def find_child(x):
    global child_node, pre_node
    if x < pre_node[-1]:
        child_node[pre_node[-1]][0] = x
        pre_node.append(x)
    else:
        for i in range(len(pre_node)-1, 0, -1):
            if pre_node[i] < x < pre_node[i-1]:
                for _ in range(len(pre_node)-i-1):
                    pre_node.pop()
                break

        child_node[pre_node[-1]][1] = x
        pre_node.append(x)

def post_order(x):
    if child_node[x][0] != 0:
        post_order(child_node[x][0])
    if child_node[x][1] != 0:
        post_order(child_node[x][1])
    print(x)


deque1 = deque()
pre_node = [1000000]
child_node = {}

while True:
    try:
        a = int(sys.stdin.readline())
        deque1.append(a)
        child_node[a] = [0, 0]
    except:
        break

root_node = deque1[0]
pre_node.append(deque1.popleft())
while deque1:
    find_child(deque1.popleft())

post_order(root_node)