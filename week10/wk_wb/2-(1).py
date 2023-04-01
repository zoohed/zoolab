for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("\n################################")

i=1 #외부제어변수
while i<6:
    j=1 #내부제어변수
    while j<i+1:
        print(j, end="")
        j+=1
    i+=1 #내부제어변수의 루틴이 끝나고 해야함
    print()