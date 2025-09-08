# 함수 정의
# 더하기 함수 만들기
# def 함수이름(매개변수): ...
# 매개변수 : 함수에 필요한 입력값(예를 들어 숫자 2개)
# 반환값 : 결과
def add(a,b):
    return a + b # 반환값
# 함수를 호출할 때, 두 숫자를 입력하고
# 호출이 끝난 후에, 경화를 보두 바아
# 함수 사용 (함수 호출)
sum = add(3, 4) #함수이름(입력값)
print('결과:', sum)


# 두 개의 숫자를 입력받아 곱한 값을 반환하는 함수를 작성하고 호출하세요
# 예) 2,5 => 10
def mul(a, b):
    return a * b
# 함수의 매개변수의 개수에 맞게 입력
result = mul(5, 5)
print('2, 5 =>', result)


# 함수의 여러가지 형태
# 입력값 없고, 반환값도 없는 함수
# 인사를 출력하는 함수 만들기
def hllo():
    print('안녕하세요')

# 함수 hello()


# 함수의 형태에따라 호출하는 방법 알기
# 입력값 없고, 리턴값만 있는 함수
# 인사를 반환하는 함수
def say():
    return 'hi'
# 리턴값이 있으면 결과를 받아야함
string =say

# # 매개변수, 입력값, 인자
# # 함수를 정의할 때는 a와 b를 '매개변수라 부른다
# def add(a+b):
#     print(a+b)
# #  함수를 호출할 때는 3과 4를 '인자'라고 부른다
# add(3, 4)


# 함수 응용하기
# 입력한 숫자만큼 '안녕하세요'출력하기
# 입력값 : 반복횟수
def hello(cnt):
    # 반복횟수는 range 안에 입력
    for _ in range(cnt): 
        print('안녕하세요')

# 매개변수가 있으면 입력값을 넣어서 함수를 호출
hello(5)



# 블록을 가지는 것 : 함수, if, for
# 블록은 들여쓰기로 구분 : space (X), tab (O)
# 블록은 변수의 scope

a = 10 # 전역 변수

if a%2 == 0:
    b = 5 # 지역 변수
    print(b)

print(a)

for n in range(10):
    print(n) # 지역 변수

def fun(x, y):
    print(x, y) #지역 변수

fun(2,3)
print(x, y)
# 함수 블록 안에서 선언된 x, y는 지역변수로
# 함수 밖에서는 사용할 수 없다




# 리스트를 입력받아 첫 번째 값을 반화하는 함수 만들기
def func(lis): #lis : 함수의 매개변수로, 함수 내부에 선언됨
    return lis[0]

#my_lis : 함수에 전달하기 위한 리스트로, 메인에 선언됨
my_lis = [10,20,30] 
#result : 함수의 결과를 저장하기 위한 변수로, 메인에 선언됨
result = func(my_lis) 
print(result)


# 문자열을 입력받아 길이를 반환하는 함수 만들기
def func(msg): #msg : 함수의 매개변수
    return len(msg)

# my_str1 : func 함수를 호출할 때 입력할 문자열
my_str1 = "abc"
my_str2 = "hello"

# result1 : func함수의 결과. "abc"의 길이를 저장할 변수
result1 = func(my_str1)
result2 = func(my_str2)