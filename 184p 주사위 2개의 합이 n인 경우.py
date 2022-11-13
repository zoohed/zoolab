#184p 주사위 2개의 합이 n인 경우
n=int(input("원하는 합 : "))
for a in range(1, 7) :
    for b in range(1, 7) :
        if a + b == n :
            print("첫번째 주사위 = %d  두번째 주사위 = %d" %(a,b))
