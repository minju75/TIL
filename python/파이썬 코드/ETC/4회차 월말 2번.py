def stone():
    global s_size,summ

    # 가장 작은 돌의 인덱스를 저장한다.
    idx = s_size.index(min(s_size))

    # 가장 작은 돌을 빼낸다.
    s_size.pop(idx)

    # 남은 돌들의 리스트의 마지막 인덱스를 저장한다.
    last_idx = len(s_size) - 1

    # 현재 남은 돌의 개수가 두개보다 많고 가장 작은 돌을 빼냈던 인덱스 값이
    # 남은 돌 리스트의 처음과 끝이 아닐 경우
    if idx != 0 and idx != last_idx and len(s_size) > 2:
        # 두개의 돌을 연속으로 뛰어넘을 수 없으므로 양측 돌들의 값을 더해주고
        # 리스트에서 제거한다.
        summ += s_size.pop(idx)
        summ += s_size.pop(idx-1)

    # 빼냈던 가장 작은 돌이 남은 돌 리스트의 가장 앞이었다면
    elif idx == 0 and s_size:
        # 바로 뒤에 있었던 돌을 빼내면서 그 값을 저장한다.
        summ += s_size.pop(idx)

    # 가장 마지막이었을 경우는 바로 앞에 있던 돌을 빼내면서 그 값을 저장한다.
    elif idx == last_idx and s_size:
        summ += s_size.pop(idx-1)


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    s_size = list(map(int,input().split()))

    # 점프로 생략할 수 있는 횟수
    jump_cnt = N-M

    # 결과를 담을 변수
    summ = 0

    # 생략할 돌의 개수만큼 함수를 호출한다.
    for _ in range(jump_cnt):
        stone()


    print(f'#{tc}',sum(s_size)+summ)