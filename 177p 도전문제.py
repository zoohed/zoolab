#177p 도전문제

#구구단 출력 while문
dan = int(input("원하는 단은 : "))
i=1
while i<=9 :
    print("%2d*%2d=%2d" %(dan, i, dan*i))
    i+=1

#구구단 출력 for문
dan=eval(input("원하는 단은 : "))
for i in range(1,10) :
    print("%d * %d = %d" %(dan, i, dan*i))

#..개인적으로 for문이 더 쉽다..
