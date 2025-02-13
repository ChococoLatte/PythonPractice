int_1 = 1234
int_2 = 123456789
int_3 = 123_456_789 # 긴 숫자를 가독성 좋게 표현(_의 위치 무관)

int_1_type = type(int_1)
int_2_type = type(int_2)
int_3_type = type(int_3)

int_bin = 0b10101   # 2진법
int_oct = 0o777     # 8진법
int_hex = 0xA5F     # 16진법

# 💡 type의 결과를 str로 감싸면 Special Variables 펼치지 않고도 바로 표시
# print 시에는 필요 없음
int_bin_type = str(type(int_bin))
int_oct_type = str(type(int_oct))
int_hex_type = str(type(int_hex))

int_plus = 123 + int_bin + int_hex # 상호간 계산 가능

import sys

# 각 정수가 차지하는 바이트 수
int_size_1 = sys.getsizeof(1)
int_size_2 = sys.getsizeof(365)
int_size_3 = sys.getsizeof(9999999)

int_size_4 = sys.getsizeof(100 ** 10) # 100의 10승
int_size_5 = sys.getsizeof(100 ** 100) # 100의 100승

# 💡 반환 : [바꿔 쑬 수 있다]고 이해
add = 5 + 3
sub = 10 - 4
mul = 7 * 2
div = 8 / 2
int_div = 9 // 2
mod = 10 % 3
pow1 = 2 ** 3
pow2 = 2 ** -3

add_type = str(type(add))
div_type = str(type(div)) # 💡 확인
int_div_type = str(type(int_div))

pow1_type = str(type(pow1))
pow2_type = str(type(pow2)) # 💡 확인

odd_even_1 = 3 % 2
odd_even_2 = 4 % 2

num = 5

num += 3 # 🛑 여기부터 브레이크포인트

num -= 4

num *= 8

num /= 4

num //= 1.5

num %= 3

num **= 3

a = 10
b = 10

# 💡 아래를 주석해제하고 다시 확인
# b += 1
# b -= 2

eq = (a == b)
ne = (a != b)
lt = (a < b)
gt = (a > b)
le = (a <= b)
ge = (a >= b)

num_1 = 3 + 4 * 5
num_2 = (3 + 4) * 5

pass