def postorder(start, end):
    if start > end:
        return

    division = end + 1 # 나눌 위치
    for i in range(start+1, end+1):
        if post[start] < post[i]:
            division = i
            break

    postorder(start+1, division-1) # 분할 왼쪽
    postorder(division, end) # 분할 오른쪽
    print(post[start])

import sys
sys.setrecursionlimit(10**6)

post = []
cnt = 0
while cnt <= 10000:
    try:
        num = int(input())
    except : break
    post.append(num)

    cnt += 1

postorder(0, len(post)-1)