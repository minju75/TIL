c, n = map(int, input().split()) # c : 닭의 수, n : 소의 수
chi = []
cow = []
for _ in range(c): # 닭이 소를 도와줄 수 있는 초
    t = int(input())
    chi.append(t)
for _ in range(n): # 소가 길을 건널떄의 초
    a, b = map(int, input().split())
    cow.append((a, b))
for i in range(c):
    for j in range(n):

