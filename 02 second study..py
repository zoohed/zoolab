#174p 1~n까지 합계

i=1
hap=0
n=int(input("정수 입력 : "))
while i<=n :
    hap+=i
    i+=1
print("합계는", hap)


#176p 구구단 출력 while문

dan = int(input("원하는 단은 : "))
i=1
while i<=9 :
    print("%2d*%2d=%2d" %(dan, i, dan*i))
    i+=1


#176p 중간점검 1번
    
#if문은 코드 안에서 조건을 판단하여 해당 조건에 맞는 상황을 수행해야 할 경우 사용한다.
#while문은 코드 안에서 반복하여 문장을 수행해야 할 경우에 사용한다.


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


#184p 주사위 2개의 합이 n인 경우
n=int(input("원하는 합 : "))
for a in range(1, 7) :
    for b in range(1, 7) :
        if a + b == n :
            print("첫번째 주사위 = %d  두번째 주사위 = %d" %(a,b))


#185p 도전문제
persons = ["Kim", "Park", "Lee"]
restaurants = ["Korean", "American", "French"]
locations = ["서울", "부산", "대전"]

for location in locations :
    for person in persons :
        for restaurant in restaurants :
            print(location + "출신의 " + person + "이 " + restaurant + " 식당을 방문")


#189p 중간점검

#1번
#break문이 반복문에서 실행되면 반복문을 빠져 나온다.


#2번
for i in range(1, 10, 1) :
    if i%3==0 : break
    print(i)
#출력 결과 (1 \n 2)


