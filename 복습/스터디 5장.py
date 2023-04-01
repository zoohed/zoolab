#5장 LAB

#213p (피자의 면적을 비교하는 프로그램)
def main():
    print("20cm 피자 2개의 면적:", get_area(20)+get_area(20))
    print("30cm 피자 1개의 면적:", get_area(30))

def get_area(radius) :
    if radius > 0 :
        area = 3.14*radius**2
    else :
        area = 0
    return area

main()


#221p (메시지를 반복하여 출력하는 프로그램)
def display(msg, count=1) :
    for k in range(count) :
        print(msg)

display("환영합니다.", 5)


#222p (이분법으로 근을 계산하는 프로그램)
def f(x):
    return (x**2-x-1)

def bisection_method(a, b, error) :
    if f(a)*f(b) > 0:
        print("구간에서 근을 찾을 수 없습니다.")
    else:
        while (b-a)/2.0 > error:
            midpoint = (a+b)/2.0
            if f(midpoint)==0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint

answer = bisection_method(1, 2, 0.0001)
print("x**2-x-1의 근:", answer)


#223p (주급을 계산하는 프로그램)
def weeklyPay(rate, hour):
    money = 0
    if (hour>30):
        money = rate*30+1.5*rate*(hour-30)
    else:
        money=rate*hour
    return money

rate=eval(input("시급을 입력하시오: "))
hour=eval(input("근무 시간을 입력하시오: "))
print("주급은 " + str(weeklyPay(rate, hour)))


#227p (여러 개의 값을 반환하는 프로그램)
def get_info():
    name=input("이름:")
    age=int(input("나이:"))
    return name, age

st_name, st_age = get_info()
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")


#231p (사각형을 그리는 프로그램)
import turtle as t
t.shape("turtle")

def square(length):
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()

square(100)
t.forward(120)
square(100)
t.forward(120)
square(100)

t.done()


#241p (터틀 그래픽 프로그램)
import turtle as t
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(200, 0)
t.goto(0, 0)

for x in range(150):
    t.goto((x, int(0.01*f(x)))

t.bye()