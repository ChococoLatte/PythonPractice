import sys

# 양수 무한대와 음수 무한대
inf_pos = float('inf')
inf_neg = float('-inf')

pos_neg = inf_pos == -inf_neg

# 무한대는 표현가능한 가장 큰 수보다 큼
inf_big_1 = inf_pos > sys.float_info.max
inf_big_2 = inf_neg < -sys.float_info.max

# 무한대에 값을 더하거나 빼도 무한대
inf_still_1 = inf_pos + 1 == inf_pos
inf_still_2 = inf_pos - 1 == inf_pos

# nan: 숫자가 아닌 것(무효한 숫자)
nan_1 = float('nan')
nan_2 = float('nan')

nan_type = str(type(nan_1))

nan_are_same = nan_1 == nan_2

# 다른 숫자와의 산술연산은 nan 반환
nan_calc_1 = nan_1 + 1
nan_calc_2 = nan_1 / 2

# 다른 숫자와의 비교 연산은 False를 반환
nan_calc_3 = nan_1 > 0
nan_calc_4 = nan_1 < 0
nan_calc_5 = nan_1 < float('inf')

# 지수
x = 3.14E5
y = 3.14E-5
# E를 소문자로 적어도 무관

# complex: 복소수
cpx_a = 2 + 3j
cpx_b = 1 - 1j

cpx_type = str(type(cpx_a))

cpx_c = cpx_a * cpx_b

cpx = 3 + 4j

# 실수부와 허수부
cpx_real = cpx.real
cpx_img = cpx.imag

# 복소수의 켤레
cpx_conj = cpx.conjugate()

# 켤레와 곱해도 자료형은 complex
mult_conj = cpx * cpx_conj
mult_conj_type = str(type(mult_conj))

# float으로 캐스팅하려면 실수부만
# cpx_to_float_1 = float(mult_conj) # ⚠️ 오류
cpx_to_float_2 = float(mult_conj.real)

# 절대값
num = -10
absolute_value = abs(num)

# 몫과 나머지
quotient, remainder = divmod(7, 2)

# 제곱
pow_result = pow(2, 3)

# 최대값과 최소값
max_num = max(3, 2, 5, 1, 4)
min_num = min(3, 2, 5, 1, 4)

# round() 예시
round_1 = round(3.6, 0)
round_2 = round(3.1415926535, 2)
round_3 = round(3.1415926535, 4)

pass