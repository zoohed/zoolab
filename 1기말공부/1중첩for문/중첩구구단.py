#중첩 for문을 활용한 구구단
for i in range(1, 10):
    for j in range(2, 10):
        print("%2d*%2d=%2d" %(j, i, i*j), end=" ")
    print()
