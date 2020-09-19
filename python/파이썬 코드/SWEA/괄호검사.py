T = int(input())
def dele(bla):
    for i in range(len(bla)):
        if bla[i] != '(' and bla[i] != ')' and bla[i] != '{' and bla[i] != '[' and bla[i] != '}' and bla[i] != ']':
            bla.remove(bla[i])
            return dele(bla)
    for i in range(1, len(bla)):
        if bla[i-1] == '(' and bla[i] == ')':
            bla.pop(i-1)
            bla.pop(i-1)
            return dele(bla)
        if bla[i-1] == '{' and bla[i] == '}':
            bla.pop(i-1)
            bla.pop(i-1)
            return dele(bla)
        if bla[i-1] == '[' and bla[i] == ']':
            bla.pop(i-1)
            bla.pop(i-1)
            return dele(bla)

    return bla
for tc in range(1,T+1):
    bla = list(input())

    if dele(bla) == []:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


paren = {'(':')', '{' : '}', '[' : ']'}
for tc in range(1, int(input()) + 1):
    arr = input()
    s = []
    ans = 1
    # 한 문자씩 읽어서 처리
    for ch in arr :
        if ch == '(' or ch == ')': # 여는 괄호
            s.append(ch)
        elif ch == ')' or ch == '(': # 닫는 괄호
            if len(s) == 0:
                ans = 0; break
            t = s.pop()
            if (ch == ')' and s[-1] != '(') or (ch == '}' and s[-1] != '{'):
                ans = 0;break
    if len(s) == 0 :
        ans = 0

    print(ans)


        # 괄호문자가 아닌 경우

            #빈 스택일 경우
            # ch와 s[-1]s 비교해서 다르다
            # 같다면 스택에 제거
    # 괄호문자가 아닌 경우
    # 빈스택인지 조사


