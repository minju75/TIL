# 과목평가 대비 HW 정리

#### 1. HTML 정의

- Hyper Text Markup Language



#### 2. CSS 정의

- Cascading Style Sheets



#### 3. CSS 개념

- HTML과 CSS 는 각자 문법을 갖는 별개의 언어이다. 
- 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.
- id 값은 유일해야하므로 중복되어서는 안된다.
- 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.



#### 4. CSS 우선순위

```HTML
!important > Inline style > id 선택자 > class 선택자 > 요소 선택자 > 소스순서
```



#### 5. HTML5에서 새롭게 추가된 시맨틱태그

```HTML
footer, header, section
```



#### 6. 선택자

'자손선택자'와 '자식선택자'의 차이를 설명하시오.

```html
/* 자손 선택자 */
div p {
  color:  crimson;
}

/* 자식 선택자*/
div > p {
  color:  crimson;
}
```

자손선택자는 하위의 모든 요소를 선택하고, 자식 선택자는 바로 아래의 요소만 선택한다. 



#### 7. CSS flex-direction

Flex-box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성해보자.

- row(기본 값) : 좌 -> 우
- row-reverse : 우 -> 좌
- column : 위 -> 아래
- column-reverse : 아래 -> 위



#### 8. align-items(css 속성값)

align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

- stretch : 부모 속성의 높이에 맞게 최대 높이로 늘여서 맞춤
- center : 수직 축의 가운데 정렬
- start : 수직 축의 시작점부터 정렬
- end : 수직축의 끝점부터 정렬



#### 9. MTV

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되는지 작성하시오.

M : Model <--> M:Model

T:Templaet <--> V:View

V:View <--> C:Controller



#### 10. Static web and Dynamic web

Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

- Static web (정적)

  - 사용자의 요청에 따라 서버안에 이미 저장 되어 있는 문서 자체를 사용자에게 제공하여 보여줌

  - 제공되는 문서의 내용이 바뀌지 않으며 모든 사용자는 같은 문서를 제공받아 똑같은 페이지를 보게 된다.

    

- Dynamic web (동적)

  - 사용자의 요청이 들어오면 웹어플리케이션 서버(장고)에서 상황에 맞는 문서를 생성해서 제공
  - 상황에 맞는 문서를 생성하므로 사용자마다 다른 문서를 제공해줄 수 있다.
  - 요청에 맞는 데이터를 DB에서 찾거나 생성하여 보여줄 수도 있다.



#### 11. model 반영하기

아래와 같이 Django에서 선언한 model을 실제 Database에 반영하는 과정을 뜻하는 용어와 이와 관련된 명령어들을 작성하시오. 

```html
class Article(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
```

`migrations`

makemigrations : model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

`python manage.py makemigrations [app이름]`

migrate : 작성된 마이그레이션 파일을 기반으로 실제 DB에 반영하기 위해 사용

`python manage.py migrate [app이름]`



#### 12. python shell

Django에서 사용 가능한 모듈 및 메서드를 대화식 pythonshell 에서 사용하려고 할 때,  어떠한 명령어를 통해 해당 shell을 실행할 수 있는지 작성하시오.

`python manage.py shell`

`python manage.py shell_plus`



#### 13. models.py를 작성한 후 마이그레이션 작업을 위해 터미널에서 작성해야하는 명령어

`python manage.py makemogrations`

`python manage.py migrate`



