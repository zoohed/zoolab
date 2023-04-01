n=int(input("수 입력:"))
fact=1
for i in range(1, n+1):
    fact*=i
    print(i, "!=", fact)

s=int(input("수 입력:"))
fact=1
for i in range(s,0,-1):
    fact*=i
    print(i, "!=", fact)