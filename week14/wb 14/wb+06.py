score=[70, 56, 89, 100, 60, 80, 65, 88]

#합구하기
hap1=0
for i in range(len(score)):
    hap1+=score[i]
print("합=", hap1)

print()

#평균구하기
hap2=0
for i in range(len(score)):
    hap2+=score[i]
    avg = hap2/len(score)
print("평균=", avg)

print()

avg2=sum(score)/len(score)
print("평균=", avg2)

print()

#분산구하기
avg3=sum(score)/len(score)
hap5=0
for i in range(len(score)):
    hap5+=(score[i]-avg3)**2
print("분산=", hap5)