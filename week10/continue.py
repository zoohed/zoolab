#2215848 박주희
i=0
while i < 10:
    i+=1
    if i%3==0:
        continue #if에 해당하면 내려가지 않고 조건으로 다시 올라간다
    print(i, end=" ") #나머지가 0이 아니면 출력한다

print("\n#########################")
i=0
while i<10:
    i+=1
    if i%3==0:
        break
    print(i, end=" ")