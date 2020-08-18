# Django

python 을 기반으로 하는 웹 백엔드 프레임워크

### 장고 설치 방법

`pip install django`

- 버전 확인 방법 `pip list`(django 3.1 확인)



### 장고 프로젝트 생성

`django-admin startproject 프로젝트명`

- 프로젝트 폴더명으로 설정 파일이 저장되는 폴더와 manage.py 파일 생성

- 외부 프로젝트 폴더명은 수정 가능하지만 내부 설정 파일 폴더는 폴더명 수정 불가

- 프로젝트 생성을 완료하며 manage.py가 있는 위치로 경로를 이동해줘야 함

  (이동을 하지 않으면 no such file 이라는 에러 발생)

- `python manage.py runserver`를 실행하여 로켓 확인

  (app 이 등록되면 로켓은 볼 수 없음)



### 장고 앱 생성

`python manage.py startapp 앱이름 (복수형 권장)`

- 앱 생성후 반드시 `settings` 파일에 앱 등록
- language_code 랑 TIME_ZONE을 한국에 맞춰서 설정



## 프로젝트 흐름

### MTV 패턴( MVC 패턴 )

- Model : DB 관리
- Template : 보여지는 페이지 관리
- View : 데이터 처리 & 관리



- 3대장

  - urls.py
  - views.py
  - models.py

  

- 코드의 작성 흐름(흐름을 잊지 말자)

  - urls.py -> views.py -> template
  - 어디에서 주소를 결정하는지!!(urls)
  - 요청이 들어오면 어떤 파일을 거치게 되는지
  - 어디에서 새로운 페이지를 만들면 되는지(templates 폴더)



- Template Variable

  - render() 사용할 때 views.py에서 정의한 변수를 template 파일로 넘겨서 사용하는 것

  - render()의 3번째 인자로 dictionary 형태로 값을 넘겨준다.

    여기에 key에 해당하는 문자열이 template 에서 사용가능한 변수명이 된다.

  - dictionary 형태로 직접 전달하는 것 보다 `context`라는 변수를 사용해서 넘기는 것이 일반적



- Variable Routing
  - 동적 라우팅 : url 주소에 변수처럼 값을 전달하는 동적인 주소를 만드는 것
  - 사용하는 이유
    - hi/justing, hi/john 같이 다양한 사람들과 인사하는 함수를 작성할 때 
      - 동적 라우팅을 쓰지 않으면 urls.py에 일일히 등록해줘야함
        - 인원이 많아지거나 누구한테 인사해야할지 모를 때 고정적인 방식은 사용하기 어려움
      - 동적 라우팅을 사용하면 뒤에 사람이름을 변수화 할 수 있다.
        - `hi/<str:name>`형식으로 나타낼 수 있음
        - views.py 에서 함수를 정의할 때 인자로 꼭 varible routing에서 선언한 변수명을 받아야 한다.
      - 변수로 사용할 수 있는 type의 종류
        - 구글에서 django url dispatcher로 검색하면 확인 가능



- djange template language(DTL)
  - DJANGO TEMPLATE에서 사용하는 내장  template system
  - 조건, 반복, 변수치환, 필터 등의 기능을 제공
  - 로직을 표현할 때 `{%%}`
  - 값을 표현할 때 `{{ }}`
  - 주석을 표현할 때 `{# #}` `{% endcomment %}`



- For 문

  - `{% for 임시변수 in 뷰로부터 전달받은iterable한 변수명>%}` `{% endfor %}`

    ```
    {% for menu in menus %}
    	<p>{{ forloop.counter }}{{ menu }}</p>
    {% empty %} #menus 가 없을 때 ( 텅 비어 있을 때 )
    	<p>메뉴가 없습니다.</p>
    {% endfor %}
    ```



- if 문

  ```
  {% if 조건문 %}
  {% elif 조건문1 %}
  {% else %}
  {% endif %}
  ```

  - 조건 연산자 사용가능

    ```
    <=
    >=
    ==
    !=
    >
    <
    in
    not in
    is
    ```



- Form

  - HTML에서 form tag

  - 입력 받은 데이터를 어딘가로 전송할 때 사용

    ```html
    <form actions""methods"">
        <input type="text" name="데이터명">
        <input type="radio" name="데이터1명">
        ....
        
        <input type="button">
        
        <input type="submit">
        <button>
            보내기
        </button> # 버튼 태그도 서브밋 역할을 함
    </form>
    <input type="text"> # form 태그 내부의 요소들과 함께 submit 불가
    ```

  - action : 데이터를 보내려는 목적지 주소

    - action="/catch" : `localhost:8000/catch/`
    - acton="/catch" : `현재주소/catch/`

  - method : http method(GET, POST)

    - GET : 주소에-query string 형식으로 데이터를 전달하는 방식(정보를 조회할 때 주로 사용)

      `localhost:8000/catch/?데이터명=데이터값&데이터명1=데이터1값&...`

  - `request`라는 장고함수 선언할 때 넣어주었던 인자에 유저가 요청한 값이 들어있음

  - 