#미세먼지 농도 예보 기준
a =  int(input("미세먼지 농도 =>"))
if 0<=a<=15 :
    print("좋음")
elif 16<=a<=35 :
    print("보통")
elif 36<=a<=75 :
    print("나쁨")
else :
    print("매우 나쁨")
