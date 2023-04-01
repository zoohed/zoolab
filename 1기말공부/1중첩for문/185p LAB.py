persons = ["Kim", "Park", "Lee", "Choi"]
restaurants = ["Korean", "American", "French", "Chinese"]

for i in persons:
    for j in restaurants:
        print(i,"이", j, "식당을 방문")


print("##################################################\n")

persons = ["Kim", "Park", "Lee", "Choi"]
restaurants = ["Korean", "American", "French", "Chinese"]
locations = ["서울", "부산", "대전", "Chinese"]
for a in persons:
    for b in locations:
        for c in restaurants:
            print(a,"이", b,"지역의", c, "식당을 방문")