n, k = map(int, input().split())
i = 1
r = 0
while i <= k:
    r = max(r, int(str(n*i)[::-1]))
    i += 1
print(r)