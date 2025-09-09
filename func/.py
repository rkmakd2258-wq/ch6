# 함수 만들기
# 문자를 입력 받아 나쁜 말이 들어오면 졸요하는 함수
# def say_nik("짱구")
# def say_nik("바보") #나쁜말을 입력하면 강제 종료!

# 식 자체는 성립되나 의도한대로 계산되지 않음
# 입력된 값이 숫자가 아니면, 더하기 계산을 할 필요가 없음
# 입력값이 숫자가 아니면 더하기를 수행할 필요가 없으므로 중간에 함수를 종료할 것
def add(n1, n2):
    if type(n1) != int or type(n2)!=int:
        print('입력받은 값이 숫자가 아닙니다')
        return


    print(f'{n1} + {n2} = {n1 + n2}')


add(3, 4)
add(5, 'bb')
add('aa', 5)
add('aa', 'bb')



# 나이를 입력받아 성인여부를 출력하는 함수를 작성하세요
# 20-> 성인입니다
# 8 -> 성인이 아닙니다
def age(n):
    if n <20 and 0 < n:
        print('성인이 아닙니다')
    elif 0 > n:
        print ('잘못된 입력입니다')
    else:
        print('성인입니다')

age(-1)
age(50)



# 사람의 정보를 출력하는 삼수 만들기
# 매개변소 : 이름, 나이, 성별
# dep info  




# 변수
# 두 a는 같으 ㄴ변수일까? 아니다
# 전역변수와 지역변수를 나누는 이유:
# scope(유효번위)로 변수를 사용할 수 있는 범위를 확인하는 것

a=1 #전역변수(어디든 사용가능)

def func(a): #지역변수(함수 내부에서만 사용 가능)
    a= a +1

func(a)
print(a)









# 더하기 함수 만들기
# def add(a,b):
#     return a+b

# 람다 함수 만들기
# 변수 = lambda 매개변수 : 변환값
# add = lambda a, b: a + b

# # 람다 함수 호출
# result = add(3,4)
# print(result)

# 꼭 써야하는가? X
# 복합 대입, 람다함수는 꽁택



# 문자열 정렬
strings = ['food', 'card', 'ba', 'aaa']

# sort : 목록을 순차적으로 정렬하는 함수
# 문자의 크기를 비교하는 함 수
# 변수 = lambda 매개변수 : 반환값
# 반환X
# 함수의 매개변수가 함수일 때, 람다식을 활용
result = strings.sort(key = lambda s : len(s))

print(result)


















