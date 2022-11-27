#244p Exercise

#01
def max(a,b):
    if a>b:
        result = a
    else:
        result = b
    return result


#02 (정답 : 10)
def main():
    print(mistery(10, 20))

def mistery(a,b):
    result = a
    if b < result:
        result = b
    return result
main()


#03 (정답 : c)
def sub(a, b, c, d):
    pass
#가능한 것
def sub(1, 2, 3, d=4)
    pass


#04
def mistery(a, b, min):
    min = a
    if b < min:
        min = b

min = 0
mistery(20, 10, min)
print(min)
#출력값 0 / 함수에서 반환되는 값이 없기 때문에 함수에 관해서 출력이 되지 않고 
#            min값을 0이라고 변수선언을 했기 때문에 0이 출력된다.


#05
x = 10
def dec():
    global x
    x = x-1

dec()
print(x)
#출력값 9 / 우선 함수 밖에서 x를 전역변수 10으로 설정하였다.
#하지만 함수 안에서 연산자 x는 지역변수를 찾는데 현재 함수에는 전역변수 x밖에 없기 때문에
#global를 사용하여 연산자 우측의 x에 10이라는 값을 넣어 출력되는 x는 9이다.


#06
x=int(input("정수를 입력하시오: "))
if x < 0 :
    y = 10
print(y)
#if문에 해당하지 않을 경우의  y의 값을 설정하지 않았다.
#if문 밖에서 따로 y에 관한 변수 선언을 해주어야 한다.


#07
def sub(a=, b=3):
    print(a, b)
#sub() -> 2, 3
#sub(a=10) -> 10, 3
#sub(5, 6) -> 5, 6
#sub(b=10) -> 2, 10


#08 (정답 : 30 -10)
def sub(a, b):
    return a+b, a-b

x, y = sub(10, 20)
print(x, y)


#09
global = 0
def sub():
    local = 1
    print(global)
    print(local)

sub()
print(global)
print(local)
#global은 예약어이기 때문에 변수로 사용할 수 없으므로 우선 _global 이런 식으로 고친다.
#local 변수가 이 코드에서 전역변수로 사용되어야하는데 현재 전역변수가 아니다.
#따라서 global local을 사용하여 전역변수로 바꿔준다.
