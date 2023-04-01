 #range함수와 list함수의 차이
for i in range(10) :
    print("우웅") #일자로 쭉 출력
    print("우웅", end="  ") #일렬로 출력 end함수는 뒤에 프린트까지 영향을 줌

for i in range(2, 10, 2) :
#2를 시작점으로 9까지 2씩 증가

list(range(2, 10, 2))
#[2, 4, 6, 8]

list(range(10, 0, -1))
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
