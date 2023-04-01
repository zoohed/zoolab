#2215848 박주희 list program
a=[50, 80, 77, 66, 35, 80, 100] #list
b=(5, 10, 12, 11, 6, 4) #tuple
#list 원소의 index로 접근
for i in range(6): #0부터 5까지라서 100의 인덱스는 6이기 때문에 출력 안됨
    print(a[i], end=" ")

print()

for i in range(len(a)) : #리스트 a 원소 개수 = 7
    print(a[i], end=" ") #0~6까지 전체가 다 출력됨
#list의 크기가 아닌 인덱스로 표기하면 list의 개수가 커질 때마다 수정하기 귀찮으니 len()을 사용한다.

print()

#list 원소를 for~each로 접근 (둘다 알고 있어야 해용 ~)
for val in a : #val이라는 변수에 리스트 a 요소의 값을 하나하나 저장함
    print(val, end=" ")

print()

#tuple 원소를 index로 접근하여 출력하는 프로그램 (list와 tuple의 사용방식은 똑같다)
for i in range(len(b)) :
    print(b[i], end=" ")

print()

#for~each로 접근
for var in b :
    print(var, end=" ")