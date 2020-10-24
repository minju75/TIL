t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    code = [list(map(int, input().split())) for _ in range(m)]
    print(code)