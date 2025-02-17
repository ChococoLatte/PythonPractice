# while문
treeHit = 0
while treeHit <10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# break문
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -=1
    print("남은 커피의 양은 %d입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# break문
a = 0
while a<10:
    a+=1
    if a%2 == 0: continue
    print(a)