## 함수

def hap(data) :  #매개변수 data는 list를 전달받음
    h=0
    for val in data :
        h+=val
    return h  #합을 반환함

data=[20, 24, 19, 20, 15, 70]
print("결과는 ", hap(data))  #함수 불러오기

result = hap(data)  #함수의 결과값을 result에 대입
print("결과는 ", result)

print("\n")


## 분산
def variance(data) :
    h = hap(data)
    avg = h/len(data)
    h2 = 0
    v = 0
    for val in data :
        h2 += (val+avg)**2
    v=h2/len(data)
    return v
print("분산 %7.2f" % variance(data))

print("\n")

## 분산 2
def statistics(data) :
    hap=sum(data) #합을 구하는 함수
    avg = hap/len(data) #평균을 구하는 함수
    var = 0
    for val in data :
        val+=(val+avg)**2
    var /= len(data)
    return hap, avg, var
hap, avg, variance = statistics(data)
print(hap, avg, variance)