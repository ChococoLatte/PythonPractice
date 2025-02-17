# 파일 읽고 쓰기

# 파일 생성하기
f = open("새파일.txt",'w')
f.close()

# 파일을 쓰기 모드로 열어 내용 쓰기
f = open("새파일.txt","w")
for i in range(1,11):
    data = "%d줄입니다.\n" %i
    f.write(data)
f.close()

# 파일을 읽는 여러 가지 방법

# readline 함수 이용하기
f = open("새파일.txt",'r')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines 함수 사용하기
f = open("새파일.txt","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read 함수 사용하기
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("새파일.txt", "a")
for i in range(11,20):
    data = "%d줄입니다.\n" % i
    f.write(data)
f.close()