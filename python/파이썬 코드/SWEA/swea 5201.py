t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    n_li = list(map(int, input().split()))
    m_li = list(map(int, input().split()))

    n_li.sort()
    m_li.sort()

    stack = []

    if n > m:
        for i in range(m):
            if n_li[-1] > m_li[-1]:
                n_li.pop()
            else:
                stack.append(n_li.pop())
                m_li.pop()
        result = sum(stack)
    else:
        for j in range(n):
            if n_li[-1] > m_li[-1]:
                n_li.pop()
            else:
                stack.append(n_li.pop())
                m_li.pop()
        result = sum(stack)

    print('#%d %d' %(tc, result))