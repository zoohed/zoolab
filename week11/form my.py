from my import module1 as n #import -> 원하는 모듈을 가지고 와서 as -> module1에 별명 부여(편의를 위해)
print("합 =", n.hap([50, 80, 78, 25, 60]))
print(n.get_area(11))

#from my 사용하는 방법
#my라는 폴더를 따로 만들어서 내가 사용할 모듈을 저장한다.
#my라는 폴더 외의 다른 폴더에서 모듈을 가져와 사용하고 싶을 때 from을 사용