#for+if문 (다시봐라 ㄹㅇ 못함 니 ㄷㄷ)
num = eval(input("정수입력 :"))
hap1=0
hap2=0
for i in range(1,num+1) :
    if i%2!=0 :
        hap1+=i
    else :
        hap2+=i
print("홀수의 합 : ", hap1)
print("짝수의 합 : ", hap2)
#print("홀수의 합 : %d \n짝수의 합 : %d" %(hap1, hap2)) 줄바꿈을 사용해서 한줄로 표현
