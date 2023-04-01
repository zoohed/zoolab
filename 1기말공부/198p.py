#01 for문
for i in range(2, 51):
    if i%2==0:
        print(i, end=" ")

print()

#01 while문
i=2
while i<51 :
    if i%2==0 :
        print(i, end=" ")
    i+=1

print("\n")

#02
myList=[11, 22, 23, 99, 81, 93, 35]

hap=0
for a in myList:
    hap+=a
print("정수들의 합은 %d" %hap)

print()

#03 for문
hap=0
for i in range(1, 100):
    if i%3==0:
        hap+=i
print("1 부터 100 사이의 모든 3의 배수의 합은 %d입니다." %hap)

#03 while문
hap=0
i=1
while i<101:
    if i%3==0:
        hap+=i
    i+=1
print("1 부터 100 사이의 모든 3의 배수의 합은 %d입니다." %hap)

print()

#04 for문
a=int(input("정수를 입력하시오: "))
for i in range(1, a+1):
    if a%i==0:
        print(i, end=" ")

print("\n")

#05
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()

#10
n=int(input("n의 값을 입력하시오:"))
i=0
hap=0
while i<n+1:
    hap+=i**2
    i+=1
print("계산값은 %d입니다." %hap)