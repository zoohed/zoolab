#246p Programming


#01
def get_peri(r=5) :
    p=2.0*3.141692*r
    return p
print(get_peri())
print(get_peri(4.0))


#02
def add(a, b) :
    return a+b

def minus(a, b) :
    return a-b

def multiply(a, b) :
    return a*b

def div(a, b) :
    return a/b

a=int(input("첫번째 정수를 입력하시오: "))
b=int(input("두번째 정수를 입력하시오: "))
print("(10+20) = ", add(a, b))
print("(10-20) = ", minus(a, b))
print("(10*20) = ", multiply(a, b))
print("(10/20) = ", div(a, b))


#03
def calc(a, b) :
    return a+b, a-b, a*b, a/b

x=int(input("첫번째 정수를 입력하시오: "))
y=int(input("두번째 정수를 입력하시오: "))
a, b, c, d = calc(x, y)
print(a, b, c, d, "이 반환되었습니다.")


#04
def getGrade(score) :
    if score>=90 :
        print("성적은 A 입니다")
    elif score>=80 :
        print("성적은 B 입니다")
    elif score>=70 :
        print("성적은 C 입니다")
    elif score>=60 :
        print("성적은 D 입니다")
    else:
        print("성적은 F 입니다")

score = eval(input("점수를 입력하세요: "))
getGrade(score)


#06
def add(a, b):
    return a+b

a=int(input("첫 번째 정수를 입력하시오:"))
b=int(input("두 번째 정수를 입력하시오:"))
print("정수 10+20의 합은?", add(a, b))
