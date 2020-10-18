# 1021 과목평가대비

### JavaScript 문법을 정리하여 Markdown 파일로 제출하 시오.

#### 1. 변수

- let : 값을 재할당 할수 있는 변수를 선언하는 키워드
  - 한번만 선언할 수 있으며 여러번 할당할 수 있다.
  
  ```js
  let x = 1
  x = 3
  ```
  
  - 재선언 할 경우 아래의 에러가 발생한다.
  
  ```js
  let x = 1
  let x = 3
  SyntaxError : Identifier 'x' has already been declared
  ```
  
  
  
  - 블록 유효범위를 갖는다.(if, for 그리고 함수 등의 중솰호{ } 내부를 의미)

```js
let x = 1
if (x === 1) {
    let x = 2
    console.log(x) // 2
}

console.log(x)	// 1
```

- const : 값이 변하지 않는 상수를 선언하는 키워드
  - 선언시 반드시 초기값을 설정해주어야한다.
  
  ```js
  const myFav = 7
  ```
  
  
  
  - 초기값을 설정하지 않으면 아래의 에러가 발생한다.
  
  ```js
  const myFav
  
  Uncaught SyntaxError: Missing initializer in cinst declaration
  ```
  
  
  
  - 상수의 값은 재할당 될 수 없고 재선언 될 수 없다.
  
  ```js
  myFav = 5
  Uncaught TypeError: Assignment to cinstant variable.
  ```
  
  ```js
  const myFav = 10
  var myFav = 10
  let myFav = 10
  
  Uncaught SyntaxError: Identifier 'myFav' has already been declared
  ```
  
  
  
  - let과 동일하게 블록 유효 범위 (block scope)를 가지고 있다.



##### 1. var : ES6 이전 변수를 선언하는 키워드

- var 키워드로 선언된 변수는 같은 var 키워드로 재선언 할 수 있다.

```js
var num = 1
var num = 2
console.log(num)	// 2
```



- 함수 유효 범위(function scope)를 가지고 있다.
- var 키워드로 선언된 변수의 범위는 현재 실행 문맥이며, 그 문맥은 둘러싼 함수 혹은 전역일 수 있다.

```js
var a = 1
var b = 2

if (true) {
    var a = 11	// 전역변수 a 덮어쓰기
    var b = 22	// if 내 지역변수
    console.log(a)	// 11
    console.log(b)	// 22
}

console.log(a)	// 11
console.log(b)	// 2
```



- var는 예기치 않은 문제를 많이 발생시키는 키워드로 절대 사용하지 않는다.



💢정리

var : 재할당, 재선언, 함수 스코프

let : 재할당, 블록 스코프

const : 블록 스코프





#### 2. 타입과 연산자

##### 2.1 타입

- Number

```js
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = NaN
```



- Boolean

```js
const inTrue = true
const isFalse = false
```



- Empty Value

  - 값이 존재하지 않음을 표현하는 값으로 null과 undefined가 있다. 큰 차이를 두지 않고 interchangeable하게 사용하도록 권장한다.
  - undefined는 값이 없을 경우 JavaScript가 할당하는 값, null은 값이 없음을 표현하기 위해서 개발자가 인위적으로 사용하는 값으로 여길 수 있다.

  ```js
  // 선언만 하고 초기화하지 않음
  let a
  console.log(a) //undefined
  
  // 의도적으로 값이 없음을 표현
  let b = null
  console.log(b) // null
  ```

  - undefined와 null은 typeof 연산자를 통해 서로 다른 값이 반환된다.

  ```js
  typeof null // object
  typeof undefined // undefined
  ```

  

##### 2.2 연산자

- 할당 연산자

```js
let c = 0
c += 10 //10 - c 에 10을 더한다.
c -= 3 // 7 - c 에 3을 뺀다.
c *= 10 // 70 - c에 10을 곱한다.
c++ // 71 - c에 1을 더한다.(증감식)
c-- // 70 - c에 1을 뺀다.(증감식)
```



- 비교 연산자

  - 문자열 비교는 영어 소문자가 대문자보다 큰 값을 가진다. 알파벳은 오름차순으로 순서로 비교한다.

  ```js
  3 > 2 // true
  3 < 2 // false
  
  'A' < 'B' // true
  'Z' < 'a' // true
  '가' < '나' //true
  ```



- 동등 연산자

  - 비교 대상이 서로 다른 타입일 경우, 비교하기 전에 가능하다면 같은 자료형으로 형변환하여 비교한다.
  - 이러한 형변환은 예기치 못한 결과를 야기할 수 있기 때문에 동등연산자의 사용은 지양한다.

  ```js
  const a = 1
  const b = '1'
  
  console.log(a==b)	//true
  console.log(a==Number(b))	//true - Number를 통해 숫자로 형변환
  ```

- 일치연산자

  - 타입과 값이 모두 같은지 비교한다. 동등 연산자와 다르게 엄격한 비교를 하기 때문에 일치 연산자를 사용하는 것을 권장한다.

  ```js
  const a = 1
  const b = '1'
  
  console.log(a===b)	//false
  console.log(a===Number(b))	//true
  ```

  

- 논리 연산자

  - boolean 타입을 연산할 수 있는 연산자로 다음과 같이 세가지 연산을 지원한다:`and, or, not`
  - `and` 연산은 &&연산자를 통해 연산한다. 모두 참일 경우 true를 반환한다.

  ```js
  true && false //false
  true && true // true
  
  1 && 0 //0
  0 && 1 //0
  4 && 7 //7
  ```

  - `or`연산은 ||연산자를 통해 연산한다. 둘 중 하나라고 참일 경우 true를 반환한다.

  ```ㅓㄴ
  false||true // true
  false||false // false
  
  1||0	//1
  0||1	//1
  4||7	//4
  ```

  - `not` 연산은 ! 연산자를 통해 연산하며, 단일 값에사용하는 단항 연산자로 해당 논리 값을 반대로 뒤집는다.

  ```js
  !true // false
  ```



- 삼항 연산자

  - 조건식이 참이면 : 앞의 값이 반환되며 그 반대일 경우 : 뒤의 값이 반환되는 연산자다.
  - 삼항 연산자의 중첩 사용은 지양하며, 일반적으로 한 줄에 표현한다.

  ```js
  true ? 1:2 //1
  false? 1:2 //2
  
  const result = Math.PI > 4 ? 'Yep' : 'Nope'
  console.log(result) // Nope
  ```

  

#### 3. 조건문과 반복문

##### 3.1 조건문

- if, else if, else

```js
const name='manager'
if (name ==== 'admin') {
    console.log('관리자님 환영합니다.')
} else if (name==='manager') {
    console.log('매니저님 환영합니다.')
} else {
    console.lg('${name}님 환영합니다')
}
```

- switch

  - switch 문은 하나의 표현식을 평가하여, 일치하는 항목의 case 절을 실행하는 조건문이다. 일치하는 항복이 없다면 default 절을 실행한다.
  - break 키워드를 통해 switch 문을 벗어난다는 것을 명시한다.

  ```js
  const name = '홍길동'
  
  switch(name) {
      case 'admin' : {
          console.log('관리자님 환영합니다.')
          break
      }
      case 'manager' : {
          console.log('매니저님 환영합니다.')
          break
      }
      default : {
          consoel.log('${name}님 환영합니다.')
      }
  }
  ```

  - break 키워드가 명시되지 않을 경우 switch 문을 벗어나지 못하고 아래의 case와 default 절까지 실행하게 된다.

  

##### 3.2 반복문

- while

```js
let i = 0

while (i<6) {
    console.log(i) //0 1 2 3 4 5 
    i++
}
```

- for

  - 사용할 변수 하나를 정의하고, 변수가 특정 조건에 대해 false가 될때까지 연산하며 반복하는 반복문이다.

  ```js
  for (let i = 0; i < 6; i++) {
      console.log(i) //0 1 2 3 4 5
  }
  ```

  

  