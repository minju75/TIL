### 0801 self_study

#### 문자열(String)

변경할 수 없고 순서가 있고 순회가능한 문자열의 다양한 조작법.

##### 조회/탐색

`.find(x)`

x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

```python
'apple'.find('p')
# 1

'apple'.find('f')
#-1
```



`.index(x)`

x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.

```python
'apple'.index('p')
#1
'apple'.index('k')
#substring not found(에러 발생)
```



#### 값 변경

`.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다. 

```python
'yay!'.replace('a', '_')
#'y_y!'
'woooowoo'.replace('0', '', 2)
#'woowoo'
```

`.strip([chars])`

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip). 지정하지 않으면 공백을 제거합니다.

```python
'        oh!\n'.stripn()
#'oh!'
'        oh!\n      '.lstrip()
#'oh!\n'
'hehehihihihihi'.rstrip('hi')
#'hehe'

```

`.split()`

문자열을 특정한 단위로 나누어 리스트로 반환합니다. 

```python
'a_b_c'.split('_')
#['a', 'b', 'c']
inputs = input().split()
print(inputs)
# 5 -> ['5']
```

`'separator'.join(iterable)`

특정한 문자열로 만들어 반환합니다. 반복가능한 컨테이너의 요소들을 separator를 구분자로 합쳐 (join())문자열로 반환합니다. 

```python
word = '배고파'
words = ['안녕', 'hello']
'i'.join(word)
''.join(words)
#'배!고!파'
#'안녕 hello'

```



#### 문자변형

`.capitalize()`, `.title()`, `.upper()`

- `.capitalize()` : 앞글자를 대문자로 만들어 반환한다.
- `.title()`: 어포스트로피나 공백 이후를 대문자로 만들어 반환한다. 
- `.upper() ` : 모두 대문자로 만들어 반환한다.

```python
a = 'hI! Everyone, i\'m kim'
a.capitalize() # "Hi! everyone, i'm kim"
a.title() #"Hi! Everyone, I'M Kim"
a.upper() #"HI! EVERYONE, I'M KIM"
```

`.lower()` , `.swapcase()`

- `lower()`: 모두 소문자로 만들어 반환한다.
- `swapcase()`: 대<->소문자로 변경하여 반환한다.

```python
a = 'hI! Everyone, i\'m kim'
a.lower() #"hi! everyone, i'm kim"
a.swapcase() #"Hi! eVERYONE, i'M KIM"
```

#### 기타 문자열 관련 검증 메소드: 참/거짓 반환

```python
.isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
```

### 리스트(list)

변경가능하고, 순서가 있고, 순회가능한 데이터 구조로서의 리스트와 조작법

#### 값 추가 및 삭제

`.append(x)`

리스트에 값을 추가할 수 있습니다.

```python
a = [1, 2, 3, 4, 5]
a.append(6)
print(a)
[1, 2, 3, 4, 5, 6]
```

`.extend(iterable)`

리스트에 iterable(list, range, tuple, string)값을 붙일 수 있다.

`.append()` 와 `.extend()`의 차이점

list.append(x)는 리스트 끝에 **x 1개를 그대로 넣습니다.**

list.extend(iterable)는 리스트 끝에 **가장 바깥쪽 iterable의 모든 항목을 넣습니다.**

`.insert(i, x)`

정해진 위치 i에 값을 추가합니다.

```python
a = [1, 2, 3, 4, 5]
a.insert(0, 'start')
print(a)
# ['start', 1, 2, 3, 4, 5]
```

`.remove(x)`

리스트에서 값이 x인 것을 삭제합니다.

```python
numbers = [1, 2, 3, 1, 2]
numbers.remove(1)
print(numbers)
#[2 ,3, 1, 2]
```

`.pop(i)`

정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환합니다.

i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

```python
a = [1, 2, 3, 4, 5, 6]
a.pop(0)
print(a)
#[2, 3, 4, 5, 6]
```

`.clear()`

리스트의 모든 항목을 삭제합니다.

```python
numbers = list(range(1, 46))
print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
numbers.clear()
print(numbers)
# []
```



#### 탐색 및 정렬

`.index(x)`

x값을 찾아 해당 index값을 반환합니다.

 ```python
a = [1, 2, 3, 4, 5]
a.index(3)
# 2
 ```

`.count(x)`

원하는 값의 개수를 확인할 수 있습니다.

```python
a = [1, 2, 5, 1, 5, 1]
print(a.count(1))
# 3

원하는 값을 모두 삭제하는 방법
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
print(a)
#[2, 3, 4]
```

`.sort()`

정렬을 합니다. 내장함수 sorted()와는 다르게 원본 list를 변형시키고 None을 리턴합니다.

```python
import random
lotto = random.sample(range(1, 46), 6)
print(lotto)
#[8, 7, 16, 14, 35, 38]

lotto.sort()
print(lotto.sort()) #None
print(lotto) #[7, 8, 14, 16, 35, 38]

lotto.sort(reverse = True)
print(lotto) #[38, 35, 16, 14, 8, 7]
```

`.reverse()`

반대로 뒤집습니다.(정렬 아님)

```python
classroom = ['Tom', 'David', 'Justin']
print(classroom) 
#['Tom', 'David', 'Justin']
classroom.reverse()
print(classroom)
#['Justin', 'David', 'Tom']

```

#### 리스트 복사

```python
original_list = [1, 2, 3]
copy_list = original_list
print(copy_list)
#[1, 2, 3]
```

