# # 입출력 장치:파일

# # 파일 열기
# # open(파일이름, 모드)
# f = open('새파일.txt', 'w')

# # 파일에 내용 쓰기
# f.write('a b c d e')

# # 파일 닫기
# # 안 써도 프로그램상 문제는 없지만 프로그램과 파일이 계속 연결되어있어 메모리가 낭비됨
# f.close()

f = open('file1.txt', 'w')
for n in range(1, 11):
    # write 함수의 매개변수는 int
    # int -> str : 1->'1'
    f.write(f'{n}\n')

f.close()


# 파일을 쓰기 모드로 열기
# 한글 입력시 인코딩 설정 추가
f = open('file2.txt','w', encoding='utf-8')

f.write('안녕하세요')

f.close()


# 1부터 10까지 출력하기
f = open('file2.txt','w', encoding='utf-8')
for i in range(1,11):
    f.write(f'{i}번째 줄입니다\n')

f.close()


# 
f = open('test.txt','w', encoding='utf-8')

f.write('hello\nhi')

f.close()

# 
f = open('score.txt','w')

f.write('80 90 70 100 60')

f.close()

# 
f = open('numbers.txt','w')
for i in range(10, 21):
    f.write(f'{i}\n')

f.close()


