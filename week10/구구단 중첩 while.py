dan=2 #while문은 초기값과 스텝이 없어 직접 설정해야함
while dan<=9 :
    i=1
    while i<=9 :
        print("%2d*%2d=%2d" %(dan, i, dan*i))
        i+=1
    dan+=1 #첫번째 while문에 포함되는 조건이라서 첫번째에 맞춰야함
    print()