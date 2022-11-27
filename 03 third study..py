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


#198p Programming

#1번 for문
for i in range(2, 51, 2) :
    print(i, end=" ")

#1번 while문
i=2
while i<51 :
    print(i, end=" ")
    i+=2


#2번
mylist = [11, 22, 23, 99, 81, 93, 35]
hap=0
for x in mylist:
    hap+=x
print("정수들의 합은 %d" %hap)


#3번 for문
hap=0
for i in range(1, 101) :
    if i%3==0 :
        hap+=i
print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." %hap)

#3번 while문
hap=0
i=1
while i<101 :
    if i%3==0 :
        hap+=i
    i+=1
print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." %hap)


#4번
n=int(input("정수를 입력하시오 : "))
print("약수 :", end=" ")
for i in range(1, n+1) :
    if n%i==0 :
        print(i, end=" ")


#5번 for문
n=int(input("정수를 입력하시오 : "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#5번 while문
n=int(input("정수를 입력하시오 : "))
i=1
while i<n+1 :
    j=1
    while j<i+1 :
        print(j, end=" ")
        j+=1
    i+=1
    print()


#10번 for문
n=int(input("n의 값을 입력하시오: "))
hap=0
for i in range(1, n+1):
    hap+=i**2
print("계산값은 %d입니다." %(hap))

#10번 while문
n=int(input("n의 값을 입력하시오: "))
i=1
hap=0
while i<=n :
    hap+=i**2
    i+=1
print("계산값은 %d입니다." %(hap))

