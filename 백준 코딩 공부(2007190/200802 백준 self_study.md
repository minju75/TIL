# 200802 백준

### 10817번 세 수

세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

```python
num = map(int,input().split())
a = sorted(num)
print(a[1])
```

### 2523번 별찍기-13

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

```python
n = int(input())
for i in range(1, n+1):
    print('*' * i)
for i in range(n-1, 0, -1):
    print('*' * i)
```

### 2446번 별찍기-9

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

```python
n = int(input())

for i in reversed(range(1, n+1)): #reverse 함수는 배열을 거꾸로 뒤집어줌
    print((' '*(n-i))+('*' * (2*i-1)))

for i in range(2, n+1):
    print((' '*(n-i))+('*' * (2*i-1)))

```

