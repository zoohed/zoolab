#난수 발생시키는 모듈
import random as r
a, b = 0, 0
a = r.randrange(1, 7)
b = r.randrange(1, 7)
print("a=%d, b=%d" %(a, b))

if a > b :
    print("a가 b를 이겼습니다.")
elif a < b :
    print("b가 a를 이겼습니다.")
else:
    print("a와 b는 비겼습니다.")
