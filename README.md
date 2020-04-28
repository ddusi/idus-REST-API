# REST API

## 개발환경

- django
- MySQL
- Python 3.7

---

## 실행방법

1. miniconda를 설치합니다. 

    [Miniconda - Conda documentation](https://docs.conda.io/en/latest/miniconda.html)

2. conda 환경변수 설정을 해줍니다. 
3. conda 가상환경을 만들어 줍니다. 

    CMD창에 다음과 같은 명령어를 씁니다.

    ```python
    conda create -n idus python=3.7 django pymysql mysqlclient
    ```

     idus라는 가상환경을 만들고, python버전은 3.7

     djnago, pymysql, mysqlclient 라이브러리들을 설치합니다.

4. conda 가상환경을 실행해줍니다. 

    ```python
    activate idus
    ```

5. 원하는 디렉토리에 이 레포지토리를 gitclone 해옵니다. 
6. `[settings.py](http://settings.py)` 파일에서 데이터베이스 설정을 해줍니다. 

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'idus',
            'USER': 'root',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': 3306
        }
    }
    ```

    idus라는 로컬 스키마를 만들어 줍니다.  

7. 테이블을 설계 해줍니다.

    ```python
    CREATE TABLE Member(
    	id INT NOT NULL AUTO_INCREMENT,
    	name VARCHAR(20) NOT NULL,
    	nick_name VARCHAR(30) NOT NULL,
    	user_id VARCHAR(20) NOT NULL,
    	user_pw VARCHAR(20) NOT NULL,
    	phone VARCHAR(20) NOT NULL,
    	email VARCHAR(50) NOT NULL,
    	gender VARCHAR(10),
    	
    	CONSTRAINT PRIMARY KEY (id)
    )
    ```

8. API 서버를 켜 줍니다. 

    ```python
    python manage.py makemigrations
    python manage.py migrate
    python manage.py
    ```

---

## 실행 예시

### urls

```python
http://localhost:8000/member
```

### 회원정보 입력 (POST)

```python
POST
Content-Type: application/json

{
    "name" : "백패커",
    "nick_name" : "아이디어스",
    "user_id" : "idus",
    "user_pw" : 1234,
    "phone" : "000-0000-0000",
    "email" : "idus@naver.com",
    "gender" : "MALE"
}
```

### 회원정보 전체 조회 (GET)

http-request

```python
GET
Content-Type: application/json

{
}
```

http-response

```python
HTTP/1.1 200 OK
Content-Type: application/json
{
    "status" : "OK",
    "message" : "요청이 성공하셨습니다.",
    "result" : {
                    "model": "rest_api_test.member",
                    "pk": 1,
                    "fields": {
                                    "name" : "백패커",
                                    "nick_name" : "아이디어스",
                                    "user_id" : "idus",
                                    "user_pw" : 1234,
                                    "phone" : "010-0000-0000",
                                    "email" : "idus@naver.com",
                                    "gender" : "MALE"
            }
}
```

### 회원정보 수정 (PUT)

```python
PUT
Content-Type: application/json

{
    "id" : "1",
    "phone" : "010-1234-5678",
}
```

### 회원정보 삭제 (DELETE)

```python
DELETE
Content-Type: application/json

{
    "id" : "1",
}
```

---

### urls

```python
http://localhost:8000/member/<int:id>
```

### 특정 회원정보 조회 (GET)

http-response

```python
HTTP/1.1 200 OK
Content-Type: application/json
{
    "status" : "OK",
    "message" : "요청이 성공하셨습니다.",
    "result" : {
                    "model": "rest_api_test.member",
                    "pk": 1,
                    "fields": {
                                    "name" : "백패커",
                                    "nick_name" : "아이디어스",
                                    "user_id" : "idus",
                                    "user_pw" : 1234,
                                    "phone" : "010-0000-0000",
                                    "email" : "idus@naver.com",
                                    "gender" : "MALE"
            }
}
```

---

### urls

```python
http://localhost:8000/member/search
http://localhost:8000/member/search?name=백패커&email=idus@naver.com
```

### 이름과 이메일주소로 회원정보 검색 (GET)

http-response

```python
HTTP/1.1 200 OK
Content-Type: application/json
{
    "status" : "OK",
    "message" : "요청이 성공하셨습니다.",
    "result" : {
                    "model": "rest_api_test.member",
                    "pk": 1,
                    "fields": {
                                    "name" : "백패커",
                                    "nick_name" : "아이디어스",
                                    "user_id" : "idus",
                                    "user_pw" : 1234,
                                    "phone" : "010-0000-0000",
                                    "email" : "idus@naver.com",
                                    "gender" : "MALE"
            }
}
```