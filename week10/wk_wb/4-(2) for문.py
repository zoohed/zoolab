#2215848 박주희 4-(2) for문
for i in range(2,31):
    for j in range(2, i+1):
        if i==j:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break