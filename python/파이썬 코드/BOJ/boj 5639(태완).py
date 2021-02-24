import sys
import bisect

sys.setrecursionlimit(100000) # 런타임 에러 해결을 위한 재귀 깊이 뚫기

def divide(s, e):
    if s >= e:
        return
    mid = s + bisect.bisect_right(arr[s+1:e], arr[s]) + 1 # bisect 함수는 이진탐색 알고리즘으로 시간 해결을 위해 사용
    divide(s+1, mid) # 왼쪽 노드
    divide(mid, e) # 오른쪽 노드
    print(arr[s])

arr = []
while True: # except 를 받지 않으면 끝없이 입력 받아야 하기 때문에 try 사용
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

divide(0, len(arr))