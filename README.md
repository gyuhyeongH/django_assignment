# django_assignment
## 1일차
### 1. args, kwargs를 사용하는 예제 코드 짜보기
```python
def example(*args, **kwargs):
    print(args)
    for key, value in kwargs.items():
        print(key)
        print(value)

example1 = example('hi',1,2,3) # 여러개의 인자 넣어보기
example2 = example(name='bob') # key-value 형태로 넣어보기
test_dict = {'name':'bob','age':11}
example3 = example(**test_dict) # 여러개의 key-value 형태 인자 넣어보기
```
```
출력 값
('hi', 1, 2, 3)
()
name
bob
()
name
bob
age
11
 *args는 튜플 형태, **kwargs는 딕셔너리 형태로 받는 것을 알 수 있다.
```
### 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
* Immutable : int, float, str, tuple 객체 수정 불가능. 추가하면 새로운 주소에 새로 생성
* Mutable : list, dict 수정해도 주소가 변하지 않음.

### 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
* 후보키 (Candidate Key) : 릴레이션을 구성하는 속성들 중에서 튜플을 유일하게 식별할 수 있는 속성들의 부분집합을 의미
    모든 릴레이션은 반드시 하나 이상의 후보키, 유일성과 최소성을 만족해야!
* 기본키 (Primary Key) : 후보키 중에서 선택한 주키(Main Key), 특정 튜플을 유일하게 구별할 수 있는 속성
  null안되고 동일한 값 중복저장 X
* 대체키 (Alternate Key) : 후보키가 둘 이상일 때 기본키를 제외한 나머지 후보키들, 보조키라고도 불림
* 슈퍼키 (Super Key) : 한 릴레이션 내에 있는 속성들의 집합으로 구성된 키
* 외래키 (Foreign Key) : 참조되는 릴레이션의 기본키와 대응되어 릴레이션 간에 참조 관계를 표현하는 도구

### 4. django에서 queryset과 object는 어떻게 다른지 서술하기
* queryset : db에서 전달받은 객체들의 모음. 테이블 내 데이터에 객체 방식으로 접근하여 쿼리를 처리.
