
# score.txt 파일을 읽고
# 합계와 평균을 구하시오

f = open('score.txt', 'r')
# 내용이 한줄밖에 없어서 read 함수 사용
text = f.read()

# read-전체내용을 문자열 하나로 가져옴
# readlines-한줄씩 읽어서 리스트로 가져옴

# 점수를 하나씩 꺼내기
# list -> for, str -> split
# 문자열을 쪼개기 위한 구분자를 선택
lis = text.split(' ')

# 총점 구하기
sum = 0 #총점을 저장할 변수

for n in lis:
    sum = sum + int(n)

print('총점:',sum)

# 평균 구하기
cnt = len(lis)

print('평균:', sum/cnt)






# numbers.txt 파일을 읽고 짝수만 출력하시오

# 읽기 모드로 파일 열기
f = open('numbers.txt','r')

# 파일 내용 읽기
lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis:
    # 짝수만 출력
    if int(line)%2 == 0:
        print(line, end='')

f.close()




