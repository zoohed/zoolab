x=10
def dec():
    global x
    x=x-1 #함수 안에서는 지역변수가 우선 / 현재 이 함수에 정의된 지역변수가 없기 때문에 global 선언을 해줘야함

dec()
print(x)



