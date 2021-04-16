def dfs(r, c):
    global answer
    if paper[r][c] == 1:
        for k in range(5, 0, -1): # 5부터 1까지
            if c_paper[k] > 0 and r+k <= 10 and c + k <= 10:
                ck = 0
                for i in range(k):
                    for j in range(k):
                        if paper[r+i][c+j] == 0:
                            ck = 1
                            break
                if ck == 1:
                    break

            if ck == 0:
                c_paper[k] -= 1
                for i in range(k):
                    for j in range(k):
                        paper[r+i][c+j] = 0

                if c < 9 :
                    dfs(r, c+1)
                elif r < 9:
                    dfs(r+1, 0)
                else :
                    sub = 0
                    for i in range(1, 6):
                        sub += 5 - c_paper[i]
                    if sub < answer:
                        answer = sub
                    return

                c_paper[k] += 1
                for i in range(k):
                    for j in range(k):
                        paper[r+i][c+j] = 1

    else:
        if c < 9:
            dfs(r, c + 1)
        elif r < 9:
            dfs(r + 1, 0)
        else:
            sub = 0
            for i in range(1, 6):
                sub += 5 - c_paper[i]
            if sub < answer:
                answer = sub
            return


paper = [list(map(int, input().split())) for _ in range(10)]
# print(paper)
c_paper = {1:5, 2:5, 3:5, 4:5, 5:5}
answer = 98765
dfs(0, 0)
if answer == 98765:
    answer = -1
print(answer)