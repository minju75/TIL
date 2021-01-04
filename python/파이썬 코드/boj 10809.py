word = input()
# print(word)
alphabet = list(range(97, 123))

for i in alphabet:
    print(word.find(chr(i)), end=" ")