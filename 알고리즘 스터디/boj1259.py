def pseudocode(): #함수를 선언
    n = int(input()) #n은 학생 수를 의미
    card = [list(map(int,input().split())) for _ in range(n)] # 학생에게 값을 입력 받아 학생 수 만큼의 2차원 리스트 생성
    total = 0 #학생이 가진 숫자 카드의 합
    b = [] # 카드의 합을 담을 빈 리스트 생성
    min_number = 100000 # 임의의 최소값 설정
    for i in range(n): # 학생 수 만큼 for문 실행
        b.append(card(i)) #card에 담겨 있는 리스트 한개한개의 합을 b 리스트에 추가
        if min_number > b[i] : # for문을 반복해 최소값 찾기
            min_number = b[i] # 가장 작은 최소값을 찾았을 때 min_number를 b[i]로 변환
            print(i) #i번째 학생이 가장 작은 최소값을 만들어내었고 따라서 이 학생이 상품수령 가능






