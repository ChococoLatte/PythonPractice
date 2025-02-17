# for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

# range 함수
a = range(10)
print(a)

marks = [90,24,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

