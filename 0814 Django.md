# Django

Django 3.1

`pip list`

* 장고 설치하기

```python
pip install django

# 특정 버전으로 받고 싶다
pip install django==3.0.8
```

* 장고 시작하기

  ```
  django-admin startproject first_webex
  ```

  * `first_webex`라는 이름으로 폴더가 생성

    * 여기 안에는 `first_webex` 폴더와 `manage.py` 생성 되어짐

      * first_webex : 프로젝트 설정 파일들이 들어 있음

      * manage.py : 장고 명령어를 실행하기 위한 파일

        `python manage.py 장고명령어`

    * 가장 바깥에 있는 프로젝트 폴더명은 수정 가능하나, setting 파일이 들어있는 폴더명은 건들이지 말자.

  * 장고 실행하기

    ```
    python manage.py runserver
    ```

* 장고 프로젝트는 Application의 집합체로 동작

  * 실제로 어떠한 역할을 해주는 친구가 바로 app.
  * 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있음.
    * 어플리케이션 : 하나의 역할 및 기능 단위로 쪼개진 형태.
      * 회원 관리 / 글 작성, 수정, 삭제 / 데이터를 수집, 분석 / ...
      * 어플리케이션을 이렇게 나뉘어야 한다 같은 기준은 없음.
      * 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.

* 어플리케이션 생성

  ```
  python manage.py startapp 앱이름(복수형)
  ```

  * 해당 앱 이름으로 폴더가 생성됨 (앱폴더)
  * 바로 할 일이 있다!!! 
    * `setting.py`에 내가 생성한 app을 등록해야함
    * Installed_app에 가장 윗줄에 등록해 준다.
    * language_code = 'ko-kr' 왠만하면 소문자로
    * time_zone = 'Asia/Seoul' 앞에만 대문자!!!!

* MTV (MVC 패턴)

  Model : 장고에서는 Model

  View : 장고에서는 Template

  Controller : 장고에서는 View

* 3대장 : 우리가 가장 밀접하게 수정하여야 하는 파일 명

  1) urls.py

  2) views.py

  3) templates (html 들)

* 

  **path('ur;패턴/', 실행이 되어야 하는 views에 있는 함수.해당 path의 별명)**

  * 많이 놓치는 부분 : url패턴 뒤에 슬래쉬

* views.py 에서 해야할 일

  * 함수를 정의 (첫번째 인자로 **request 필수**!!)
  * **return은 꼭 필요!**
    * render : 주로 과 함께 respose 할 때 사용하는 함수

* template 에서 해야할 일

  * 폴더 명은 반드시 `templates` 인 것을 확인



## 여기 까지가 기본 수정할 파일들 조작 방법

## 여기서 부터는 본격 장고 동작 정의 방법

* Template Variable

  * html 과 같은 template에서 view.py 에서 준비한 변수를 가져다가 쓰는 방법

  * render() 세번째 인자로 `{'key':value}`와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져올 수 있다.

    ```python
    context = {'key': value}
    return render(request, 'index.html', context)
    ```

    ```html
    {{ key }} 이렇게 value를 보여줄 수 있다.
    ```

     

* Variable Routing(동적 라우팅)

  * url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

    주소 요청 : `http://127.0.0.1:8000/hello/문자열`

    urls.py

    ```
    path('hello/<str(타입):name(저장되는 변수명)>/', views.hello),
    ```

    * int : 숫자 형식으로 받음.

    views.py

    ```
    def hello(request, name(저장되는 변수명):
    	print(name)
    	context = {
    		'name': name,
    	}
    	return render(request, 'hello.html', context)
    ```

    template(hello.html)

    ```
    <body>
    이름은 : {{ name }}  # context 의 key 값을 사용하면 value 를 출력한다.
    </body>
    ```

    

* DTL (tag와 filter)

  * 로직을 사용할 때 표현 형식 : `{% %}`

  * 값을 표현할 때는 : `{{ }}`

  * 주석으로 나타내고 싶을 때는 : `{# #}`or {% comment %}주석 할 내용 {% endcomment %}

    ```
    <!--<h1>{#{ i * 2 }#}</h1>-->
    {% comment %}<h1>{{ i * 2 }}</h1>{% endcomment %}
    ```

    

  * for 태그

    * 반복을 위한 태그

      ```
      {% for 임시변수 in iterable 한 객체 %}
      {% endfor %}
      ```

    * for empty

      ```
      {% for 임시변수 in iterable 한 객체 %}
      	값이 하나라도 있으면 여기가 실행
      {% empty %}
      	출력할 값이 없으면 출력.
      {% endfor %}
      ```

  * if 태그

    * 조건을 구분 하기 위한 태그

      ```
      {% if 조건문 %}
      {% elif 조건문 %}
      {% else %}
      {% endif %}
      ```

  * 나머지 기타 유용한 dtl 문서를 참고.(구글에서 찾을 때 바로 찾는 키워드 **django built in template**)



* Form

  * HTML form 의미

  * 입력 받은 데이터를 어딘가로 보낼 때 사용

    ```
    # action : 보내려는 목표  # method : http method(get / post)
    <form action="" method="GET">
    	
    	input 데이터를 입력 받게 적절히 코딩 하면 됨
    	
    	# 오락실 버튼
    	<input type="button">
    	
    	# 미사일 버튼
    	<input type="submit">
    			or
    	<button></button>
    </form>
    ```

    



JSON 파일

파이썬의 딕셔너리와 구조가 똑같다.

{key: value}

단, 차이점은 json 은 binary 형식으로 저장된다.

(쉽게 말하면 문자열로 저장이 된다.

더 쉽게 말하면 10 vs '10')

