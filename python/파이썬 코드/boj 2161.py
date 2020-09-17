n = int(input())
num = [i for i in range(1, n+1)]
# print(num)
stack = []
while len(num) != 1:
    stack.append(num.pop(0))
    num.append(num.pop(0))

# for i in stack:
print(*stack, num[0])
