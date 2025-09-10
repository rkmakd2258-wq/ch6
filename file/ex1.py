# 키보드로 값 입력받기

a = input() # 사용자가 입력할 때까지 대기
# print('입력받은 값), a

# 숫자 두 개 입력받기
# input함수로 받는 값은 str
n1 = input('첫번째 숫자를 입력하세요: ')
n2 = input('두 번째 숫자를 입력하세요: ')
print(int(n1)*int(n2))

# 사용자로부터 이름과 나이를 입력받아 자기소개를 출력하세요
name = input('이름을 입력하세요: ')
age = input('나이를 입력하세요: ')
print('저는 ',age,'살 ', name, '입니다.')


# 사과 가격과 수량을 입력 받아 총 가격 계산하세요
price = input('사과 가격을 입력하세요: ')
cnt = input('사과 수량을 입력하세요: ')
print('사과 총 가격은', int(price)*int(cnt),'원 입니다.')


# 시험 점수를 입력 받아 합격 여부를 출력하세요
# 60점 이상 : 합격
# 60점 미만 : 불합격
score = input('시험 점수를 입력하세요: ')
if int(score) >= 60:
    print('합격')
else:
    print('불합격')


# 학생의 나이를 입력 받아 버스 요금을 계산하세요
# 어린이(0~12세):1000원
# 청소년(13~18세):1500원
# 성인(19세 이상);2000원
age = input('나이를 입력하시오.')
if int(age)>=0 and int(age)<=12:
    print('1000원')
elif int(age)>=13 and int(age)<=18:
    print('1500원')
else:
    print('2000원')


# 문자를 계속 입력 받다가 0이 들어오면 종료하세요
# 조건을 잘 모르겠을 때 :조건식을 True 로 두기  
while True:
    text = input('값을 입력하세요:')
    if text == '0':
        break
    
# 매개변수를 줄바꿈으로 대신 공백으로 바꾸기
# print(calue, end='/n')
print(1, end=', ')
print(2, end=', ')
print(3, end=', ')