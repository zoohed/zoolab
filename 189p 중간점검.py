#189p 중간점검

#1번
#break문이 반복문에서 실행되면 반복문을 빠져 나온다.

#2번
for i in range(1, 10, 1) :
    if i%3==0 : break
    print(i)
#출력 결과 (1 \n 2)
