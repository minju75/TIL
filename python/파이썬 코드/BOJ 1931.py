n = int(input()) # 회의의 수
conference_li = [] #회의의 시작 시간과 끝나는 시간 받아오기
for i in range(n):
    s, e = map(int, input().split())
    conference_li.append([s, e])
conference_li = sorted(conference_li, key=lambda a: a[0])
conference_li = sorted(conference_li, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in conference_li:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
