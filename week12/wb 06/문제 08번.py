#2215848 박주희 문제 8번
def cal_bmi(weight,height):
    height*=0.01 #cm로 입력받은 키를 m로 변경
    bmi=(weight/(height**2)) #bmi=체중(Kg)/신장(m)**2
    if bmi<18.5:
        print("저체중입니다.")
    elif 18.5<=bmi<25.0:
        print("표준입니다.")
    elif 25.0<=bmi<30:
        print("과체중입니다.")
    else :
        print("비만입니다.")

#몸무게와 키를 키보드로 부터 입력받기 위해 코드 작성
weight=eval(input("몸무게 : "))
height=eval(input("키 : "))
cal_bmi(weight, height) #설정한 bmi 함수를 불러 실행시킨다.
