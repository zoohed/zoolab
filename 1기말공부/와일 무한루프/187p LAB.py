i=2
while i<50 :
    j=2
    while j<i+1:
        if i==j:
            print(i, end=" ")
        elif i%j==0:
            break
        j+=1
    i+=1