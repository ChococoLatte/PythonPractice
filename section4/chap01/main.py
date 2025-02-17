# 함수
def add(a,b):
    return a+b

a = 3
b = 4
c = add(a,b)
print(c)

# 일반적인 함수
def add(a,b):
    return a+b

a = add(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'

b = say()
print(b)

# 리턴값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

add(3,4)

# 입력값도, 리턴값도 없는 함수
def say():
    print('Hi')

say()

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result+=i
    return result

result = add_many(1,2,3)
print(result)

# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1,b=2,c=3)
print_kwargs(name='foo', age=3)

# 람다 함수
add = lambda a,b:a+b
result = add(3,4)
print(result)

