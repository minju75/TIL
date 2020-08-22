# 0804 강의

## Solving Club

### 4828번 min, max

```python
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1,T+1):
    n = int(input())
    tc_list = list(map(int,input().split()))

    max_num = tc_list[0]
    min_num = tc_list[0]

    for num in tc_list:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num

    print('#%d %d' %(t, max_num - min_num))
    #print(max_num - min_num)
```





### 4834번 숫자카드

```python
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1,T+1):
    n = int(input())
    tc_list = list(map(int, input()))
    a = tc_list.count(tc_list[0])
    b = tc_list[0]
    for num in range(len(tc_list)):
        if tc_list.count(tc_list[num]) > a:
            a = tc_list.count(tc_list[num])
            b = tc_list[num]
        elif tc_list.count(tc_list[num]) == a and  b < tc_list[num]:
     
            b = tc_list[num]

        else:
            max_num = tc_list[0]


    print ('#%d %d %d' %(t, b, a))
```



### 4835번 구간합

```python
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for t in range(1,T+1):
    #n = list(map(int,input().split()))
    n, m = map(int, input().split())
    a = list(map(int,input().split()))
    e = list()
    
    for i in range(n-m+1):
        e.append(sum(a[i:i+m]))
    b = max(e)
    c = min(e)
    d = b - c

    print('#%d %d' %(t, d))
```



### 전기버스

```python
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    k, n, m = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    s = 0

    move = k
    while s < n:
        if s + move == n:
            break
        elif s + move in a:
            count += 1
            s += move
            move = k
        else:
            move -= 1
            if move == 0:
                count = 0
                break

    print('#%d %d' %(i, count))
```

