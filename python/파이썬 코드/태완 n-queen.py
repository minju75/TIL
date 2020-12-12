def build_queen(n, N) :
    global result
    if n == N :
        result += 1
        return
    else :
        for i in range(N) :
            row[n] = i
            for j in range(n):
                if row[j] == row[n] or (row[n] - n) == (row[j] - j) or (row[n] + n) == (row[j] + j):
                    break
            else : build_queen(n+1, N)

s = int(input())
result = 0
row = [300] * s
build_queen(0, s)
print(result)