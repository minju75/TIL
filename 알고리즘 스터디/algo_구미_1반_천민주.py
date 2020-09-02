t = int(input())
for tc in range(1, t+1):
    n, m, d = map(int,input().split())
    a = n//2
    ta = [[0]*n for _ in range(n)] # 먼저 n*n 배열로 이루어진 2차원 리스트 생성
    b = []
    for i in range(n):
        for j in range(n):
            #for q in range(a):
                ta[a][a] = m
                ta[0][j] = (m+(d*a)) # 맨 윗부분의 경우 동일한 숫자가 입력되기 때문에 규칙을 찾아서 설정
                if j == 0 : # j 가 0인 경우는 왼쪽 벽면 왼쪽 벽면 또한 위와 마찬가지로 규칙을 찾아서 설정
                    ta[i][j] = (m+(d*a))
                elif j == (n-1): # j 가 n-1인 경우는 오른쪽 벽면을 의미, 위와 마찬가지로 가장 마지막에 올 숫자를 규칙을 통해서 설정
                    ta[i][j] = (m+(d*a))
                elif i == 1 and j != 0 and j != (n-1): #j 가 n-2인 경우는 오른쪽에서 2번째! 이 경우에는 전부 동일한 숫자가 와야 함으로 규칙으로 숫자 설정
                    ta[i][j] = (m+(d*(a-1)))
                elif j == 1 :
                    ta[i][j] = (m+(d*(a-1)))
                elif j == 2:
                    ta[i][j] = (m+(d*(a-2)))
                    if i == 1 :
                        ta[i][j] = (m+(d*(a-2)))

                else :
                    ta[i][j] = (m+(d*(a-2)))

    for w in range(a+1): #행의 합을 구하기 위해서는 ta에 담아놓은 리스트들의 합을 b 라는 list에 append한다.
        b.append(sum(ta[w]))
    for q in range(n, a+1, -1): #다시 역순으로 적어줘야하기 때문에 range의 설정을 반대로 해서 b 라는 리스트에 append한다.
        b.append(sum(ta[w]))
    print('#%d' %tc, end='')
    print(b)





