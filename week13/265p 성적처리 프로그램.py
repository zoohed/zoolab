#2215848 박주희 성적 처리 프로그램
score = [78, 95, 88, 65, 100]
hap=0
for i in range(len(score)) :
    hap += score[i]
print("합 =", hap, "평균 =", hap/len(score))