# 이진탐색
def tree(n):
    global cnt
    if n <= N:
        tree(n*2) #좌측
        m_tree[n] = cnt
        cnt += 1 #카운트에 증가
        tree(n*2 + 1) # 우측

t = int(input()) # 테스트케이스의 갯수
for tc in range(1, t+1):
    N = int(input())
    m_tree = [0 for _ in range(N+1)]
    # print(tree)
    cnt = 1
    tree(1)
    print('#%d %d %d' %(tc, m_tree[1], m_tree[N//2]))
