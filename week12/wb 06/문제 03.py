a=0 #전역변수
def func1():
    print(a)
def func2():
    a=111 #지역변수
    print(a)
func1()
func2()