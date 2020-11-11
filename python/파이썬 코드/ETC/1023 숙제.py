n = list(str(input()))
byte = []
for i in range(0, len(n), 7):
    byte.append(n[i:i+7])

sum = []
for z in range(0, len(byte)):
    sum.append(int(byte[z][0])*64 + int(byte[z][1])*32 + int(byte[z][2])*16 + int(byte[z][3])*8 + int(byte[z][4])*4 + int(byte[z][5])*2 + int(byte[z][6])*1)

print(sum)