n=int(input("숫자를 입력하세요:"))
i=1
hap=0
while i<=n :
    hap+=i**2
    i+=1
print("결과는 %d 입니다." %(hap))