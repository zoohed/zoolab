n1=eval(input("수1=> "))
n2=eval(input("수2=> "))
print("더하기=> ", n1+n2)
print("빼기=> ", n1-n2)
print("나누기=> ", n1/n2)
print("나누기(몫)=> ", n1//n2)
print("나머지값=> ", n1%n2)
print("곱하기=> ", n1*n2)
print("제곱=> ", n1**n2)

print("############################################")

x, y = 10, 30
x+=y
print("x=%d, y=%d" %(x,y))
x*=y
x, y=y,x
print("x=%d, y=%d" %(x,y))