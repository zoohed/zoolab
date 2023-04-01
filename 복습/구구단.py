#구구단
dan=eval(input("단을 입력 : "))
for i in range(1,10) :
    print("%d * %d = %d" %(dan, i, dan*i))
