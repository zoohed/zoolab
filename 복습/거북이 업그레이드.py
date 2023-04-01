#거북이 for문
import turtle as t
t.shape("turtle")
n=eval(t.textinput("거북이는 귀여웡", "몇각형할꺼양?"))
for i in range(n) :
    t.forward(100)
    t.left(360/n)
t.done()
