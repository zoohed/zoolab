#215848 박주희 4-(1) for문
for i in range(2,101): #외부변수 i -> 2부터 100까지의 숫자
    for j in range(2, i + 1): #내부변수 j의 역할 -> 2부터 i까지 i의 약수를 알아보는 변수
        if i==j: #만약 i와 j가 같다면 / 즉 i
            print(i, end=" ")
        elif i%j==0:
            break
