ORM 작성 SQL 같이 보자
-- 1. user 테이블 전체 데이터 조회
-- User.objects.all()

-- 2. id 가 19인 사람의 age를 조회하시오.
-- User.objects.filter(id=19).values('age')

-- 3. 모든 사람의 age를 조회하시오.
-- User.objects.all().values('age')

-- 4. age가 40 이하인 사람들의 id와 balance를 조회하시오. 
-- User.objects.filter(age__lte=40).values('id', 'balance')

-- 5. last_name 이 '김'이고 balance가 500 이상인 사람들의 first_name을 조회하시오.
-- User.objects.filter(last_name='김', balance__gte=500).values('first_name')

-- 6. first_name이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오
-- User.objects.filter(first_name_endswith='수', country='경기도').values('balance')

-- 7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.
-- User.objects.filter(balance__gte=2000 | age__lte=40).count()

-- 8. phone이 '010'으로 시작하는 사람들의 총원을 구하시오.
-- User.objects.filter(phone__startwith='010').count()

-- 9. 이름이 '김옥자'인 사람의 행정구역을 경기도로 수정하시오.
-- users =  User.objects.filter(last_name='옥자', first_name='김')
-- for user in users:
--     user.country = '경기도'
--     user.save()

-- User.objects.filter(last_name='옥자', first_name='김').update(country='경기도');

-- 10. 이름이 '백진호'인 사람을 삭제하시오.
-- User.objects.filter(last_name='진호', first_name='백').delete()

-- 11. balance를 기준으로 상위 4명의 first_name, last_name을 조회하시오.
-- User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]


-- 12. phone 에 '123'을 포함하고 age가 30미만인 정보를 조회하시오.
-- User.objects.filter(phone__contains='123', age__lt=30)

-- 13. phone에 '010'으로 시작하는 사람들의 행정구역을 중복없이 조회하시오.
-- User.objects.filter(phone__startswith='010').values('country;).distinct()

-- 14. 모든 인원의 평균 age를 구하시오.
-- User.objects.aggregate(Avg('age'))

-- 15. 박씨의 평균 balance를 구하시오.
-- User.objects.filter(last_name='박')/aggregate(Avg('balalnce'))

-- 16. 경상북도에 사는 사람 중 가장 많은 balance 액수를 구하시오.
-- User.objects.filter(country='경상북도').order_by('-balance')[0]

-- 17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.
-- User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')