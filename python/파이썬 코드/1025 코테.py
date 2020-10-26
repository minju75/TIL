word = list(input())
# print(word)
word_2 = []
n = len(word)
for i in range(n):
    word_2.append(word[n-1])
    word_2.append(word[n-2])
    break
for i in word_2:
    print(*word_2)
    print()
    break
