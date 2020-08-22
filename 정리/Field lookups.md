# Field lookups

- 구글링 키워드 : `django queryset`
- `필드명_필드룩업`
- exact : 대소문자 전부 일치해야함.
- iexact : 대소문자는 상관없이 일치하면 됨.
- contains : 해당글자가 어느위치던지 포함되어 있으면 됨
- startswith : 해당 글자로 시작하는 것만
- endswith : 해당글자로 끝나는 것만
- gt / gte/ lt / lte : 비교연산자

### 실습

- 제목이 first이고 한개만 가져와라

  ```
  Article.objects.filter(title="first").first()
  ```

  - 해당 모델 클래스로 값이 리턴

  

- 정렬을 하고 싶을 때(오름차순&내림차순)

  ```
  # 오름차순
  Article.objects.order_by('pk')
  Article.objects.order_by('title')
  
  #내림차순
  Article.objects.order_by('-pk')
  Article.objects.order_by('-title')
  ```



- QuerySet으로 리턴을 받았을 때

  - QuerySet은 List와 유사함.
  - indexing & slicing

  ```
  #indexing
  Article.objectx.all()[2]
  Article.objectx.all()[-1] #음수는 지원하지 않음
  
  #slicing
  Article.objects.all()[:2]
  ```

  