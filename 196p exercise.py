#196p exercise


#2번
for i in range(0, 10, 2) :
    print(i)

#2번 while문 변경
i=0
while i<10 :
    print(i)
    i+=2


#3번
for i in range(-2, -6, -1) :
    print(i, end=" ")

#3번 while문
i=-2
while i>-6 :
    print(i, end=" ")
    i+=-1


#4번
sum=0
i=0
while i<100:
    sum+=i
    i+=1
print(sum)


#5번(결과 : 6번)
for x in range(10) :
    if x > 5 : continue
    if x > 8 : break
    print("Hello World!")


#6번
i=0
while i < 10 :
    print(i)
#i의 값이 10이 되는 경우 즉 false에 해당하는 부분이 없어 무한루프이다.


#7번(총 11번 반복)
i=0
while i<=10 :
    print("Hi !")
    i+=1


#8번(결과 : 100)
x=0
while (x<100) :
    x+=2
print(x)


#10번
numbers = [10, 20]
items = ["TV", "Phone"]
for x in numbers:
    for y in items:
        print(x, y)
#출력결과
#10 TV
#10 Phone
#20 TV
#20 Phone

    
