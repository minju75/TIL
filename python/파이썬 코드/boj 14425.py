import sys

# 시간초과

n, m = map(int, sys.stdin.readline().split())
li = []
li_2 = []
for _ in range(n):
    word = list(sys.stdin.readline())
    li.append(word)
for _ in range(m):
    word_2 = list(sys.stdin.readline())
    li_2.append(word_2)
# print(li)
# print(li_2)
cnt = 0
for i in range(m):
    for j in range(n):
        if li_2[i] == li[j]:
            cnt += 1
print(cnt)