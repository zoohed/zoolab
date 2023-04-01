#2215848 박주희 문제 8번 (함수 : BMI 지수 구하기)
def cal_bmi(weight,height):
    height*=0.01
    bmi=(weight/(height**2))
    if bmi<18.5:
        print("저체중입니다.")
    elif 18.5<=bmi<25.0:
        print("표준입니다.")
    elif 25.0<=bmi<30:
        print("과체중입니다.")
    else :
        print("비만입니다.")

weight=eval(input("몸무게(kg) : "))
height=eval(input("키(cm) : "))
cal_bmi(weight, height)
