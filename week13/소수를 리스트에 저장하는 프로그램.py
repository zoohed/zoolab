#2215848 박주희 소수를 리스트에 저장하는 프로그램
def prime(num):
    isPrime=True
    for i in range(2, num):
        if num%i==0:
            isPrime=False
            break
    return isPrime

aList=[] #aList는 리스트 데이터 구조로 선언
for i in range(2, 100):
    if prime(i):
        aList.append(i) #해당하는 소수가 계속 추가됨

print(aList) #aList에는 현재 소수가 다 들어가 있음
print(len(aList)) #몇개의 요소가 있는지
print(sum(aList)) #요소들의 합

print("\n###############################################\n")

avg = sum(aList)/len(aList) #평균
hap = 0
for i in range(len(aList)) :
    hap+=(aList[i]-avg)**2
print("평균=%7.4f, 분산=%9.3f" %(avg, hap/len(aList)))
