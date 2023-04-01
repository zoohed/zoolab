#2215848 박주희 : 함수와 모듈에 관한 프로그램
def get_area(r) : #원의 면적과 둘레를 구하는 함수
    area = 3.14159*r**2 #면적
    cir = 3.14159*2*r #둘레
    return  area, cir #반환하는 값이 면적과 둘레 두개임

def fact(n=1) : #매개변수에 디폴트값 설정
    f=1
    for i in range(1, n+1) :
        f*=i
    return f

def hap(var) :
    s=0
    for val in var : #var값을 val에 계속 기억시킨다
        s+=val
    return s

#합 함수 호출하기
#print("합 =", hap([50, 15, 60, 85, 10]))