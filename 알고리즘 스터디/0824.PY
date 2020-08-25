t = int(input())
for i in range(1, t+1):
    case, n = input().split()
    q = list(map(str,input().split()))
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    A = []
    cnt = 0
    print(case)
    for x in range(len(q)):
        for r in range(10):
            if num[r] == q[x]:
                cnt += 1
            print(num[r]*cnt, end=" ")