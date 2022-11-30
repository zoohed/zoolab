#247p Programming

#09
def get_GCD(a, b):
    i=min(a,b)  #두 수 중 더 작은 값을 i에 저장한다.
    while True :  #i가 두 수의 공통된 약수인지 확인한다.
        if a%i==0 and b%i==0:
            return i  #공통된 약수라면 이 값을 결과값으로 돌려주고 종료한다.
        i-=1  #아니라면 i를 1만큼 감소시키고 다시 반복문으로 돌아간다.
        
a=int(input("첫 번째 정수:"))
b=int(input("두 번째 정수:"))
print(get_GCD(a, b))


#10
def prime(num) :
    isPrime = True 
    for i in range(2, num) :
        if num%i==0 :
            isPrime = False
            break
    return isPrime

val=2
while val<=100:
    if prime(val):
        print(val, end=" ")
    val+=1


#12
def getSorted(x, y):
    a, b=min(x, y), max(x, y)
    return a, b

x=int(input("첫 번째 정수:"))
y=int(input("두 번째 정수:"))
print(getSorted(x, y))


#16
def darw_line():
    t.forward(100)
    t.backward(100)

import turtle as t
t.shape("turtle")

for i in range(12):
    darw_line()
    t.left(30)



#Workbook 01

#01-(1) (정답 : 1 2 4 5)
i=0
while i<6:
    i+=1
    if i%3==0:
        continue
    print(i, end=" ")


#01-(2) (정답 : 합 = 55)
i=1
hap=0
while i <=10:
    hap+=i
    i+=1 #무한루프 방지
print("합 =", hap) 


#02-(1)
#for문
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

#while문
i=1 
while i<6:
    j=1 
    while j<i+1:
        print(j, end="")
        j+=1
    i+=1 
    print()


#02-(2)
#for문
    for i in range(10):
    for j in range(i, 10):
        print("*", end='')
    print()

#while문
i=0
while i<10:
    j=i
    while j<10:
        print("*", end='')
        j+=1
    i+=1
    print()


#02-(3)
n=int(input("숫자를 입력하세요:"))
i=1
hap=0
while i<=n :
    hap+=i**2
    i+=1
print("결과는 %d 입니다." %(hap))


#03-(1)
import turtle as t
t.circle(100) #반지름 100인 원을 그린다
t.left(60) #60도 만큼 왼쪽으로 회전시킨다
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.done()


#03-(2)
#while문으로 변경
import turtle as t
i=0
while i<6:
    t.circle(100)
    t.left(60)
    i+=1


#04-(1)
#for문
for i in range(2,101):
    for j in range(2, i + 1):
        if i==j: 
            print(i, end=" ")
        elif i%j==0:

#while문
i=2
while i<101: 
    j=2
    while j<i+1:
        if j==i: 
            print(i, end=" ") 
        elif i%j==0: 
            break
        j+=1
    i+=1


#04-(2)
#for문
for i in range(2,31):
    for j in range(2, i+1):
        if i==j:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break

#while문
i=2
while i<31:
    j=2
    while j<i+1:
        if j==i:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break
        j+=1
    i+=1
            break
t.done()



#Workbook 02

#01
def sum(v1, v2):
    result = v1+v2
    return result
print(sum(v1, v2)) #함수호출


#02
def func(v1, v2=0, v3=0):
    return v1+v2+v3
#print(func(1)) -> 1
#print(func(1, 2)) -> 3
#print(func()) -> v1 값이 정의되어 있지 않아서 오류발생


#03
a=0
def func1():
    print(a)
def func2():
    a=111
    print(a)
func1() # (정답 : 0)
func2() # (정답 : 111)


#04 (정답 : 30-10)
def sub(a, b):
    return a+b, a-b
x, y = sub(10, 20)
print(x, y)


#05 (정답 : 9)
x=10
def dec():
    global x
    x=x-1
dec()
print(x)
#함수 안에서는 지역변수가 우선이다.
#함수 안 x=x-1처럼 함수 안 연산자는 지역변수를 찾는데
#현재 함수에는 전역변수 밖에 없어 함수 안에서 global x 선언을 하여
#전역변수를 지역변수처럼 사용하게 한다.


#06
def square(n):
    return n**2
print('3의 제곱은:', square(3))
print('4의 제곱은:', square(4))


#07
def draw_square(size) :
    for i in range(4) :
        t.fd(size)
        t.left(90)
        size += 5

import turtle as t
t.shape("turtle")
t.color("blue")

for i in range(8) :
    draw_square(i*20+5)
t.done()


#08 (비만도 함수 작성)
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
