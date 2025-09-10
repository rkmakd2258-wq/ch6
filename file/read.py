# 반대로 파일의 내용을 읽어오기

# 읽기모드로 파일 열기
# 파일이름, 모드(w, r)
f=open('새파일.txt','r')

# 파일의 내용 읽어오기
# 읽기 함수들 중에서 readlines는 결과를 리스트로 반환
# 결과는 리스트로 저장됨
# read는 파일의 내용을 문자열 하나로 반환
text = f.read()
print(text)

# 문자열 안에 있는 알파벳을 하나씩 꺼내기
# 함수의 인자:구분자
# split 함수는 공백을 기준으로
# 문자열을 쪼개고 결과를 리스트로 반환

# 리턴값이 있을 때:
lis = text.split('  ') # 공백
# 리턴값이 없을 때:
# lis.sort()
print(lis)

# 알파벳 하나씩 출력하기
for ch in lis:
    print(ch)

# 사용이 끝났으면 닫기
f.close()


# 반대로 파일 읽어오기
# 입력장치: 키보드 -> 파일
# 키보드에서 값 입력받기
# input()
# 파일에서 값 읽어오기
# f.read()

# 파일이름, 모드
f = open('file1.txt', 'r')

# read 함수로 내용 읽어오기
# 결과를 리스트로 반환
# 내용에는 줄바꿈이 포함됨 \n
lis = f.readlines()

# 한줄씩 출력하기
for line in lis:
    # end 매개변수 값 변경
    print(line, end = '')

# print 함수에는 end라는 매개변수가 있고
# 기본값이 \n 
print('1', end = '\n')

print(lis)


# 파일 내용 일거오기
# 파일이름, 모드
# 파일에 한글이 있으면 인코딩 추가
f= open('file2.txt', 'r', encoding='utf-8')

# read 함수로 내용 읽어오기
# readlines는 리스트로 반환
lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis:
    # end 매개변수의 값 변경
    # '\n' -> ' '
    print(line, end = '')


# file2.txt의 현재 내용 : 1~10줄
# 새로운 내용 추가  : 11~21줄

# 내용 추가 -> 쓰기 모드(w 또는 a)
# 'w' 모드는 기존의 내용을 덮어씌움
# 'a' 모드는 이전 내용 뒤에 새로운 내용이 추가됨 
f= open('file2.txt', 'a', encoding='utf-8')

# 10번줄 뒤에
# 11~20번 줄을 추가
for i in range(11,21):
    f.write(f'{i}번째 줄입니다\n')

    f.close



