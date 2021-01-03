n = int(input())
heap = []
max_num = 0
pp = []
for _ in range(n):
    num = int(input())
    if num == 0 :
        heap.append(num)
        if len(heap) == 0:
            pp.append(0)
        else:
            for i in range(len(heap)):
                if max_num <= heap[i]:
                    max_num = heap[i]
                    pp.append(max_num)
    else:
        heap.append(num)
print(pp)