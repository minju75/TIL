# # 재귀함수
# for i in range(3): # i = 0, 1, 2
#     print('hello')
#
# # 재귀 호출로 단순 반복을 구현
# # 재귀 호출이 몇번 행해졌는지는 알 수 있어야 한다.
# # 재귀 호출의 종료는 매개변수를 기준으로 판단한다.
#
# def printHello(i): # i 를 이용해서 종료를 판단
#     if i == 3:     #
#         pass
#     else:
#         print('Hello')
#         printHello(i + 1)
#
# printHello(0)
#
# def printHello(i, n): # i 를 이용해서 종료를 판단
#     if i == n:     #
#         pass
#     else:
#         print(i, '>Hello')
#         printHello(i + 1, n)
#
# printHello(0, 3)

cnt = 0
def printHello(i, n):
    if i == n:
        global cnt; cnt += 1
    else :
        printHello(i+1, n)

n = 3
printHello(0, n)
print(cnt)


