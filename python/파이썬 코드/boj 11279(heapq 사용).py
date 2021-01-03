import heapq
import sys
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0 :
        heapq.heappush(heap, (-num)) # heap에 -num 을 추가(heappop은 최소값을 출력하기 때문에 음수를 넣기)
    else:
        try:
            print(-1 * heapq.heappop(heap)) # 힙에서 가장 작은 원소에다가 -를 더하면 최댓값이 되므로 print하고 pop 시켜줌
        except:
            print(0)