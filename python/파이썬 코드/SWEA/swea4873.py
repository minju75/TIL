# t = int(input())
# for tc in range(1, t+1):
#     sentence = list(input())
#     stack = []
#     for i in range(len(sentence)+1):
#         stack.append(sentence[i])
#     # print(stack)
#     # print(sentence)
#         if len(stack) >= 2:
#             if stack[-2] == stack[-1]:
#                 stack.pop(-1)
#
#     result = len(stack)
#
#     print('#%d %d' %(tc, result))

T = int(input())

for tc in range(1,T+1):
    sentence = list(input())
    # print(sentence)
    stack = []
    for i in range(len(sentence)):

        if stack and sentence[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(sentence[i])
        print(stack)

    # print(len(stack))
    print(f'#{tc}',len(stack))