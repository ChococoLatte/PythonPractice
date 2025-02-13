from decimal import Decimal

flt_1 = 3.14
flt_2 = 1.0
flt_3 = 123_456.789 # 역시 _ 사용 가능

flt_1_type = str(type(flt_1))
flt_2_type = str(type(flt_2))
flt_3_type = str(type(flt_3))

# 부동소수점 방식상 오차 자주 있음
a = 0.2 + 0.3
b = Decimal('0.2') * Decimal('0.7') # 파이썬에서 오차 없이 실수들간의 연산을 하기 위해 Decimal 사용
c = 0.4 - 0.3
d = 0.9 / 0.3
e = 0.9 % 0.6

# 소수부가 2의 거듭제곱인 숫자간 연산은 오차 없음
f = 0.25 * 0.5
g = 0.5 + 0.25 + 0.125 + 0.0625
h = 0.0625 / 0.125

int_num = 123
flt_num = 123.0

result = int_num + flt_num
result_type = str(type(result)) # int와 float의 연산은 float 반환

# 명시적 explicit 캐스팀: 개발자가 코드로 명시하여 변환
# int
a = 24
a_type = str(type(a))

# float으로 캐스팅
b = float(a)
b_type = str(type(b))

# 다시 int로 캐스팅
c = int(b)
c_type = str(type(c))

# 💡 float을 int로 캐스팅하면 자동 내림
d = int(3.14)
d_type = str(type(d))

# 암시적 implicit 캐스팅: 조건에 의해 자동으로 변환
# int
e = 10
e_type = str(type(e))

# 나누기와 음수 제곱은 float으로 암시적 캐스팅
f = e / 2
f_type = str(type(f))

g = e ** -2
g_type = str(type(g))

# int와 float간의 게산도 float으로 암시적 캐스팅
h = e + 1.0
h_type = str(type(h))

pass