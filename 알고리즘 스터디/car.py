icp = {'*': 2, '+': 1, '(': 0}
isp = {'*': 2, '+': 1, '(': 3}
for tc in range(1):
    n = int(input())
    car = list(input())
    num = []
    special = []
    for i in range(n):
        if car[i] != '*' and car[i] != '+' and car[i] != '(' and car[i] != ')':
            num.append(car[i])
        else:
            special.append(car[i])
            if car[i] == ')':
                for j in range(len(special)-1, -1, -1):
                    if special[j] == '(':
                        num.extend(special[j+1:len(special)-1])
                        special = special[:j]
            else:
                while spe
                        len(special) >=2 and icp[car[i]] > isp[special[-2]]:
                    num.append[car[i]]



