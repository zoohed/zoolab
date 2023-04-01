#2215848 박주희 while문을 활용한 turtle
import turtle as t
t.circle(100) #반지름 100인 원을 그린다
t.left(60) #60도 만큼 왼쪽으로 회전시킨다
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.circle(100)
t.left(60)
t.done()

print("/n############################")

import turtle as t
i=0
while i<6:
    t.circle(100)
    t.left(60)
    i+=1
t.done()