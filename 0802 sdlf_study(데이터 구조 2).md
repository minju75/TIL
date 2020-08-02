# 데이터구조2

### 세트(Set)

변경 가능하고 순서가 없고 순회 가능한 데이터 구조로서의 세트와 조작법

#### 추가 및 삭제

`.add(elem)`

elem을 세트에 추가합니다.

`.update(*others)`

여러가지의 값을 추가합니다.

인자로는 반드시 iterable 데이터 구조를 전달해야합니다.

`.remove(elem)`

elem을 세트에서 삭제하고 없으면 keyError가 발생합니다. 

`.discard(elem)`

elem을 세트에서 삭제하고 없어도 에러가 발생하지 않습니다.

`.pop()`

임의의 원소를 제거해 반환합니다. 

```python
a = {'사과', '바나나', '수박', '아보카도'}
a.pop()
print(a)
#{'바나나', '사과', '아보카도'}
```

### 딕셔너리

변경가능하고 순서가 없고 순회가능한 Key:Value 페어(pair)의 자료구조

데이터 구조로서의 딕셔너리와 조작법

#### 조회

`.get(key[, default])`
key를 통해 value를 가져옵니다. 

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None입니다. 

#### 추가 및 삭제

`.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다. default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다. 

```python
my_dict = {'apple' : '사과', 'banana' : '바나나'}
my_dict.pop('apple')
print(my_dict)
#{'banana' : '바나나'}
```

`.update()`

값을 제공하는 key, value로 덮어씁니다.

```python
my_dict = {'apple':'사과', 'banana':'바나나', 'melon':'멜론'}
my_dict.update(apple='사과아')
print(my_dict)
#{'apple': '사과아', 'banana': '바나나', 'melon': '멜론'}

```

### 딕셔너리 순회(반복문 활용)

딕셔너리에 for문을 실행하면 기본적으로 다음과 같이 동작합니다.

```python
grades = {'john':80,, 'eric':90, 'justin':90}
for student in grades:
    print(student)
    
#john
#eric
#justin
```

딕셔너리의 key를 접근할 수 있으면 value에도 접근할 수 있기 때문입니다. 따라서 딕셔너리의 value를 출력하기 위해서는 아래와 같이 작성합니다.

```python
for student in grades:
    print(grades[student])
    
#80
#90
#90
```

- dictionary에서 `for`를 활용하는 4가지 방법

```python
# 0. dictionary 순회(key 활용)
for key in dict:
    print(key)
    print(dict[key])
    
#1. '.keys()' 활용
for key in dict.keys():
    print(key)
    print(dict[key])
    
#2. '.values()' 활용
for val in dect.values():
    print(val)
    
#3. '.items()' 활용
for key, val in dict.items():
    print(key, val)
```

#### 딕셔너리 순회

혈액형 검사한 결과가 담긴 blood_types이 주어졌을 때, 해당 딕셔너리를 순회하며, key와 value를 출력해보세요.

```python
blood_types = {'A' : 40, 'B':11, 'AB':4, '0':45}
for blood_type in blood_types:
    print(f'{blood_type}형은 {blood_types[blood_type]}명입니다.')
    
#A형은 40명입니다.
#B형은 11명입니다.
#AB형은 4명입니다.
#O형은 45명입니다.
```

#### 딕셔너리 구축하기(counter)

리스트가 주어질 때, 각각의 요소의 개수를 value값으로 갖는 딕셔너리를 만드세요.

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

title_counter = {}
for title in book_title:
    if title in title_counter:
        title_counter[title] += 1
        
    else:
        title_counter[title] = 1
        
print(title_counter)

#{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}


# .get() method 사용하기
title_counter = {}
for title in book_title:
    title_counter[title] = title_counter.get(title, 0) +1
    
print(title_counter)

#{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}


# .count() 사용하기
title_counter = {}
for title in book_title:
    title_counter[title] = book_title.count(title)
    
print(title_counter)

#{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

```



`get(key[, default])`

key가 딕셔너리에 있는 경우 key에 대응하는 값을 돌려주고, 그렇지 않으면 default를 돌려준다.

#### Dictionary comprehension

dictionary도 comprehension을 활용하여 만들 수 있습니다.

###### 활용법

`iterable`에서 `dict`를 생성할 수 있습니다. 

{키 : 값 for 요소 in iterable}

dict{키 : 값 for 요소 in iterable}

```python
cubic = {x : x ** 3 for x in range(1, 8)}
print(cubic)
#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7:343}
```



#### Dictionary comprehoesion + 조건

List comprehension과 유사하게, 조건문에 참인 식으로 딕셔너리를 생성합니다. 

##### 활용법

{키 : 값 for 요소 in iterable if 조건식}

{키 : 값 if  조건식 else 값 for 요소 in iterable}

#elif는 가음과 같이 사용해야 합니다. (if else 열거)

{키: 값 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable}

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
result = {key: value for key, value in dusts.items() if value > 80}
print(result)
#{'대전': 82, '중국': 200}
```

