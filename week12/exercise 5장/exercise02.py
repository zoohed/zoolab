def main(): #매개변수 생략가능
    print(mistery(10, 20))

def mistery(a, b):
    result = a
    if b < result:
        result = b
    return result

main()