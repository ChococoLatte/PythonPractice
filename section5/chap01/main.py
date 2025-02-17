# 클래스 정의
class Calculator:
    # 생성자(constructor)
    def __init__(self):
        # 인스턴스 속성(instance attribute)
        self.result = 0

    def add(self, num):
        self.result +=num
        return self.result

# 인스턴스 생성(생성자 호춣)
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal2.add(3))

print()

# 클래스의 상속
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.pow())

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

b = SafeFourCal(4,0)
print(b.div())

# 클래스 변수
class Family:
    lastname = "김" # 클래스 변수

print(Family.lastname)