#2215848 박주희 함수 프로그램
def get_area(r) : #콜론빼먹지마 / 함수이름은 우리가 변수설정하듯 하면 됨(변수규칙지켜서)
    area=3.14159*r**2
    return area #area의 결과를 되돌려주겠다 (리턴해서 반환해야하는 값 또는 변수 ?)

#함수 사용하기(호출하기)
result = get_area(7)
print("원의 면적 :", result)

print("\n########################")

print(get_area(15))  #result를 사용하지 않고 바로 출력

#호출되는 순서 잘 이해해야한다
#get_area 함수를 호출한다
#전달되는 수를 "인자"라고 표현 / 즉 7이라는 인자가 매개변수 r로 전달된다. 아규먼트 = 인자
#함수는 7이라는 값을 가지고 순서대로 계산을 한 후 result에 다시 반환해준다. ..?
