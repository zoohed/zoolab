#185p 도전문제
persons = ["Kim", "Park", "Lee"]
restaurants = ["Korean", "American", "French"]
locations = ["서울", "부산", "대전"]

for location in locations :
    for person in persons :
        for restaurant in restaurants :
            print(location + "출신의 " + person + "이 " + restaurant + " 식당을 방문")
