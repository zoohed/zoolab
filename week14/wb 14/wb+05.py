list1=list() #시험 함수랑 리스트의 차이 알아야한다.
for num in range(2, 10):
    is_Prime=True
    for i in range(2, num) : #(2, 2)는 돌아가지 않음
        if num%i==0:
            is_Prime = False
            break
    if is_Prime :
        list1.append(num)
print(list1)