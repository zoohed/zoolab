##소수를 구하는 함수
def prime(num) :
    isPrime = True #왜 대문자? isPrime을 우선 True로 두고 ?
    for i in range(2, num) :
        if num%i==0 :
            isPrime = False #이 조건에 맞으면 isPrime은 False가 된고 깬 다음 리턴으로 넘어간다 ?
            break
    return isPrime

print(prime(6))
print(prime(5))
#4를 입력 / 일단 isPrime=4 / for문에 4를 넣고 조건문으로 넘어감 / if 조건문에 걸리기 때문에 isPrime은 False고 False출력
#5를 입력 / 일단 isPrime=5 / for문에 넣고 조건문으로 넘어감 / if문에 안걸려서 True를 리턴


##2부터 50까지 소수와 합성수 출력
for val in range(2, 51):
    print(val, "소수" if prime(val) else "합성수")

##2부터 100까지 소수만 출력
val=2
while val<=100:
    if prime(val):
        print(val, end=" ")
    val+=1

##200부터 500까지 소수만 출력
for val in range(200, 501):
    if prime(val):
        print(val, end=" ") #print()가 if 안에 들어가 있어야지 ~ ....
