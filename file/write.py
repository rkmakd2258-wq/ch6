# 파일을 쓰기 모드로 열기
f = open('new.txt', 'w')
f.write('hello world')
f.close()

# 위 코드를 간단하게 작성하기(위 코드와 같다)
# with를 사용하면 마지막에 자동으로 close가 실행됨
with open('new.txt', 'w') as f:
    # 블록에는 수행하고 싶은 코드 작성
    f.write('hello world')