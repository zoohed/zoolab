#176p 구구단 출력 while문
dan = int(input("원하는 단은 : "))
i=1
while i<=9 :
    print("%2d*%2d=%2d" %(dan, i, dan*i))
    i+=1
