# arr = ['A', 'B', 'C', 'D', 'E'];
# n = len(arr)
# pick = []
# for i in range(0, n - 2):
#     pick.append(arr[i])
#     for j in range(i+1, n - 1):
#         pick.append(arr[j])
#         for k in range(j+1, n):
#             pick.append(arr[k])
#             print(pick)
#             pick.pop()
#         pick.pop()
#     pick.pop()
#

arr = ['a', 'b', 'c', 'd', 'e'];
n = 5
r = 3
pick = []
def comb(k, s): # s : for 문의 시작 인덱스
    if k == r:
        print(pick)
    else:
        for i in range(s, n): # n, r, k
            pick.append(arr[i])
            comb(k + 1, i + 1)
            # 재귀 호출
            pick.pop()

comb(0, 0)

