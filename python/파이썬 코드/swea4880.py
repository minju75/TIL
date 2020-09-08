def game(s, e):
    if s == e: # 한명인 그룹
        return s

    # 절반씩 나누어서 게임 실행
    # 앞 부분 승자, 뒷부분 승자 각각 구하기
    # 대결해서 승자를 결정
    center = (s+e)//2
    v1 = game(s, center) # 승리자
    v2 = game(center+1, e) #승리자 2

    # 두 그룹의 승자 중 이긴 사람을 반환
    # 1가위 2바위 3보
    v1_card = cards[v1]
    v2_card = cards[v2]
    if v1_card == 1 : # 가위일때
        if v2_card == 2:
            return v2
        else :
            return v1

    elif v1_card == 2: # 바위일때
        if v2_card == 3:
            return v2
        else :
            return v1

    elif v1_card == 3: # 보 일때때
        if v2_card ==1:
            return v2
        else :
            return v1




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int,input().split()))
    result = game(0, n-1)
    print("#{} {}".format(tc, result+1))
