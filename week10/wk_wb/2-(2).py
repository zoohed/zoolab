for i in range(10):
    for j in range(i, 10):
        print("*", end='')
    print()

print("#############################")

i=0
while i<10:
    j=i
    while j<10:
        print("*", end='')
        j+=1
    i+=1
    print()