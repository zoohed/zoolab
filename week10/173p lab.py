TARGET = 2000 #대문자는 상수정의
moeny = 1000
rate = 0.07
year = 0
while moeny < TARGET :
    moeny += moeny*rate
    year += 1
print(year, "년")