n=eval(input("숫자를 입력하세요 : "))
hap=0
for n in range(1, n+1):
    hap+=n**2
print("결과는 %d 입니다." %hap)
