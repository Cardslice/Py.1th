print("예제 11-14")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")
def getGrade(score) :
    if score>=90 : return('A')
    elif  score>=80 : return('B')
    elif  score>=70 : return('C')
    elif  score>=60 : return('D')
    else : return('F')
score = [88, 75, 92, 64, 82]
total = 0
for jumsu in score :
    total = total + jumsu
    grade = getGrade(jumsu)
    print("%3d : %2s" % (jumsu, grade))
avg = total / len(score)
print("\n 리스트 평균 :", avg)
