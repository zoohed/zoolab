#총임금 계산
work = int(input("근무시간을 입력=>"))
wage = int(input("시간당 임금을 입력=>"))
total = 0
if work > 40 :
    total = 40*wage + (work-40)*wage*1.5
else :
    total = work*wage
print("총임금=>", total)
