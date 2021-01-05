import heapq

n = int(input())
card_li = []
for _ in range(n):
    heapq.heappush(card_li, int(input()))

if len(card_li) == 1:
    print(0)
else:
    total = 0
    while len(card_li) > 1: #  아니면 sort 정렬?
        fir = heapq.heappop(card_li)
        sec = heapq.heappop(card_li)
        total += fir + sec
        heapq.heappush(card_li, fir + sec)
    print(total)