#리스트함수
a=[20, 30, 15, 14, 20]
s=0
for data in a : #리스트를 사용하는 방법
    print(data, end=" ")
    s+=data
print("합 :", s)
print(sum(a))

for i in range(5) : #인덱스를 사용하는 방법
    print(a[i], end=" ")

hap=0
for i in range(len(a)) : #인덱스를 사용하되 범위를 계속 고치지 않고 가능 len() 사용
    print(a[i], end=" ")
    hap+=a[i]
print("합=", hap)
