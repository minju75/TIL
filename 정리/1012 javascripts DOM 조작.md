# DOM 조작

- 화면으로 표시되는 HTML을 조작이 가능
- selector를 이용해서 조작을 한다.
  - `querySelector`를 이용해서 id, class, 태그를 선택해서 조작할 수 있다.
    - `getElementyById`는 수업시간에서는 사용하지 않을 예정
      - live 속성 때문에
- 정리
  1. 선택한다.
  2. 변경한다.



###  EventListener

- 이벤트

  - 브라우져에서 일어나는 일

- 이벤트 리스너

  - `~하면 ~한다`

  - 특정한 이벤트가 발생하면, 할 일을 실행한다. 

    `이벤트타겟.addEventListener(이벤트타입, 할일)`

- `preventDefault()`

  - 기존에 발생하는 동작을 동작하지 않게 설정(submit)



### 식별자(identifier)

- 변수명은 식별자라고도 불림.
- 규칙
  1. 반드시 문자, 달라($) 또는 밑줄로 시작해야 한다!!(숫자나, `-` 로 시작할 수 없다.)
  2. 대소문자를 구분한다.
  3. 예약어는 사용할 수 없다.(const, function, class, ....)
- 스타일
  - 카멜케이스 (lowerCamelCase)
    - 객체, 변수, 함수 선언 시 사용
  - 파스칼 케이스(UpperCamelCase)
    - 클래스, 생성자
  - 대문자 스네이크 케이스(UPPER_CASE)
    - 상수 : 변수의 속성이 변하지 않는 것



### Hoisting

- var로 선언된 변수는 선언 이전에 참조할 수 있는 현상

```
console.log(name)
var name = '홍길동'

console.log(age)
let age = 10
```





### String

- JS 에서 문자열을 표현하는 방법

```javascript
const str1 = '홀 따옴표 사용'
const str2 = "쌍 따옴표 사용"

str1 + str2 //2개의 문장을 한 문장으로 합침

cosnt str3 = "줄 바꿈
은 허락되지 않는다"

//escape squence
const str4 = "줄바꿈은 \n 이렇게 해야합니다."

//Template literal (ES6+) 백틱 (': 물결표 쉽트 없이.')
const str 5 = '안녕하세요
줄바꿈도 가능합니다.'

const num = 100
const str8 = '$(num) - $(str1)'
```

- 리터럴
  - 리터럴이라는 단어는 값을 프로그램 안에서 직접 지정한다라는 의미
  - 





## Switch

```js
const name = '홍길동'

switch(name) {
    case 'admin': {
        console.log('관리자 모드')
        break
    }
    case 'manager': {
        console.log('매니저 모드')
        break
    }
    default: {
        console.log(`${name} 님 환영합니다.`)
    }
}
```



### for문

```javascript
for (let i = 0; i < 6; i++){
    console.log(i)
}
```



### 화살표함수

```javascript
const arrow = function (name) {
    return 'hello! $(name)!!'
}

//1. function 키워드를 삭제하고 화살표를 추가한다.
1. const arrow = (name) => {
    return 'hello! $(name)!!'
}

//2. 매개변수가 하나일 때는 괄호를 생략할 수 있다.
2. const arrow = name => {
    return 'hello! $(name)!!'
}

//3. {} & return 생략 (body에 표현식이 1개인 경우)
3. const arrow = name => 'hello! $(name)!!'

//연습 코드
const exam = function() {
    return 'hello, world!'
}

//1
const exam = () => {
    return 'hello, world'
}

//2 skip
//3.
const exam = () => 'hello, world'
or
const exam = _ => 'hello, world'
```





### function 키워드 호이스팅

```javascript
// 선언식일때는 동작
add(2, 7)
function add(a, b) {
    return a + b
}

// 표현식일때는? 동작하지 않음
sub(7, 2)
var sub = function (num1, num2) {
    return num1 - num2
}
```



### 함수의 object 축약형

```javascript
let obj = {
    name : 'ssafy',
    sayHi: function() {
        console.log('hello')
    }
}

obj.sayHi() //'hello'

//ES6+
let obj2 = {
    name:'ssafy',
    // 함수의 object 축약형
    sayHi : function () {
        console.log('hi!!')
    }
}

obj2.sayHi() //'hi!!'
```





### JSON (JavaScript Object Notation)

JavaScript Object 형태를 가지는 `문자열`

#### object -> JSON(string)

```javascript
const objData = {
    coffee:'Americano',
    icecream:'Bravo corn',
}

const jsonData = JSON.stringfy(objData)
console.log(typeof(jsonData))
```

#### JSON -> object

```javascript
const objData2 = JSON.parse(jsonData)
console.log(typeof(objData2))
```



Helper -> 자주 사용하는 로직을 재활용할 수 있게 만든 일종의 라이브러리



### forEach

- exercise

  ```js
  // 배열 안에 있는 정보를 곱해서 그 넓이를 areas 배열에 저장.
  const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 }
  ]
  const areas = []
  ```

  - 풀이코드

    ```js
    images.forEach(function (img){
        areas.push(img.height * img.width)// { height: 10, width: 30 },
    })
    console.log(areas)
    ```



### map

- exercise

```js
// 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드세요.

const newNumbers = [4, 9, 16]
```

- 풀이코드

  ```js
  const newArray = newNumbers.map(function (num){
      return num ** 0.5
  })
  
  const newArray = newNumbers.map(Math.sqrt)
  ```

  ```js
  const areas2 = images.map(function (img) {
      return img.height * img.width
  })
  console.log(area2)
  ```

  



### filter

```js
const products = [
    { name : 'cucumber', type:'vegetable'},
    { name : 'banana', type:'fruit'}
    { name : 'carrot', type:'vegetable'}
    { name : 'apple', type:'fruit'}

]

const fruits = products.filter(function (product) {
    return product.type === 'fruit'
})
console.log(fruits)
```

- exercise

  ```js
  //numbers 배열 중 50보다 큰 값들만 모은 배열 filternumbers를 만드세요.
  const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
  
  const filteredNumbers =  numbers.filter(function (num) {
      return num > 50
  })
  ```





```js
const products = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'},
    
]

//타입이 베지터블인 것을 찾아보자
const select = products.find(function(product){
    return product.type === 'vegetable'
})
select #{ name : 'cucumber', type : 'vegetable'} 처음 만난 하나만 반환함.
```



### sum

```js
const products = [
    { name : 'cucumber', type : 'vegetable'},
    { name : 'banana', type : 'fruit'},
    { name : 'carrot', type : 'vegetable'},
    { name : 'apple', type : 'fruit'},   
]
// 베지터블이 있는지 확인
const someVegetable = products.some(function(product){
    return product.type === 'vegetable'
})
console.log(someVegetable) #true

const someWater = products.some(function(product){
    return product.type === 'water'
})
console.log(someWater) #false
```

```js
//requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

```



### every

```js
// users 배열에서 모두가 submited 인지 여부를 hassubmited에 저장하세요.
const users = [
    { id: 21, submmited: true },
    { id: 33, submmited: false },
    { id: 712, submmited: true},
]

//풀이코드
const hasSubmitted = users.every(function (user) { 
    return user.submitted 
})
console.log(hasSunmitted)
```



### reduce

```js
// 주어진 baseUrl 문자열 뒤에 필수 요청 변수인 api 의 key - value 값을 KEY=value 의 형태로 더하여 요청 url을 만드세요. URL에서 요청 변수는 & 문자로 구분합니다. 
const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
const api = {
  'key': 'API_KEY',
  'targetDt': '20200115'
}

const apiUrl = Object.entries(api).reduce(function (url, api) {
    return url + '${api[0]}=${api[1]}&'
}, baseUrl)
console.log(apiUrl)
```

