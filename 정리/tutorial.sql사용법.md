# tutorial.sql

```python

-- 한줄 주석
/* 여러줄 주석 */

--테이블 정보 조회
SELECT*FROM classmates;

--data 입력
INSERT INTO classmates(nsame, age)
VALUES('honggildong', 30);

-- 모든 칼럼을 입력 할 때는 컬럼명 생략 가능
INSERT INTO classmates
VALUES ('hong gil dong', 30, 'seoul');

-- 컬럼의 위치는 변경 가능. 단, value 도 위치 확인
INSERT INTO classmates (age, name)
VALUES (23, 'hong gil dong');

-- id를 보고 싶을 떄
SELECT ROWID, *FROM classmates;


--테이블 다시 정의(id, not null 적용)
-- 기존 테이블 삭제
DROP TABLE classmates;

--테이블 재정의
CREATE TABLE classmates (
  id INT PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

--rowid를 사용하기 위해 우리가 정의한 id 삭제
CREATE TABLE classmates (
  id INT PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);


--INSERT INTO 로 값을 한번에 넣는 방법
INSERT INTO classmates VALUES('HONG', 30, 'SEOUL'),('KIM', 23, 'DAEJEON'),
('PARK', 23, 'GWANGJU'),('LEE', 23, 'GUMI');

--classmate에서 id와 name을 가져오고 싶다면
SELECT rowid, name FROM classmates;

--원하는 레코드 갯수만큼 가져올려면
SELECT rowid, name FROM classmates LIMIT 2;


--세번째 있는 값 하나만 가져오고 싶다면
SELECT rowid, name FROMclassmates LIMIT 1 OFFSET;


--주소가 서울인 사람만 가져오고 싶다면
SELECT rowid, name FROM classmates WHERE address;

-- age 값을 중복없이 가져오고 싶을 때
SELECT DISTINCT age FROM classmates;


--id 가 4인 레코드를 삭제
DELETE FROM classmates
WHERE rowid=4;


--id가 4 인 레코드의 이름은 hong 주소는 jejudo로 수정
UPDATE classmates SET name="HONG", address="jejudo" WHERE rowid=4;

--user data를 새롭게 테이블로 작성
--선행되어야 할게 users.csv 파일이 db 파일과 동일한 위치에 있어야함
-- sqlite에서 사용하는 dot command
.tables # 모든 테이블 확인
.import users.csv users # users라는 테이블이 생성되는데 기준이 users.csv 파일을 기반으로 생성
SELECT*FROM users; # 모든 데이터 확인

-- 30 살 이상인 데이터만 가져오고 싶을 때
SELECT*FROM users WHERE age >= 30;

-- 30살 이상이고 이름만 필요할 떄
SELECT first_name FROM users WHERE age >= 30;

--30살 이상이고 성이 김인 사람의 성과 나이만 가져온다면?
SELECT last_name, age FROM users WHERE age >= 30 and last_name='김';

-- users 테이블의 모든 레코드 갯수
SELECT COUNT(*) FROM users;


--30살 이상의 평균 나이는
SELECT AVG(age) FROM users WHERE AGE>=30;


-- 계좌 잔액이 가장 높은 사람과 그 금액은?
SELECT MAX(balance), last_name FROM users;


--30살 이상인 사람의 계좌 평균 잔액은?
SELECT AVG(balance) FROM users WHERE age >= 30;

--20대인 사람은?
SELECT * FROM users WHERE age LIKE '2_';

--지역번호가 02 인 사람
SELECT * FROM users WHERE phone LIKE '02-%';

--이름이 준으로 끝나는 사람
SELECT * FROM users WHERE first_name LIKE '%준';

--중간번호가 5114인 사람
SELECT * FROM users WHERE phone LIKE '%-5114-%';

--users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
SELECT * FROM users ORDER BY age ASC LIMIT 10; 

--나이순, 성의 오름차순으로 10명만(ASC 생략 가능)
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

--계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 뽑아보면?
SELECT last_name, first_name FROM users 
ORDER BY balance DESC LIMIT 10;

--각 성(last_name)씨가 몇명씩 있는지 조회하시오
SELECT last_name,COUNT() FROM users GROUP BY last_name;

--각 성씨의 명수를 확인 AS를 이용해서 컬러명을 설정
SELECT last_name,COUNT(*) AS name_count FROM users
GROUP BY last_name;
```

