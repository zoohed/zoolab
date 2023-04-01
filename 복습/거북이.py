import turtle as t
t.shape("turtle")
t.color("purple")
n=eval(input("몇각형을 원하시나요? :"))
for i in range(4): #반복문은 i(제어변수)를 사용하셔야지요 ㅜㅜ
    t.forward(200)
    t.right(360/n)
t.done()