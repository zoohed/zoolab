#두 과목의 평균으로 학점 구하기
score1 = int(input("점수1=>"))
score2 = int(input("점수2=>"))
avg = (score1+score2)/2
grade = ""
if avg >=90 :
    grade = "A"
elif avg >=80 :
    grade = "B"
elif avg >=70 :
    grade = "C"
elif avg >=60 :
    grade = "D"
else:
    grade = "F"
print("당신의 평균은 %5.2f이고 %c학점입니다." %(avg, grade))
