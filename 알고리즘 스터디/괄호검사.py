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