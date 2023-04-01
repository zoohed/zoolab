#2215848 박주희 4-(2) while문
i=2
while i<31:
    j=2
    while j<i+1:
        if j==i:
            print("%2d : 소수" %i)
        elif i%j==0:
            print("%2d : 합성수" %i)
            break
        j+=1
    i+=1

#와일문은 초기값과 스탭이 없기 때문에