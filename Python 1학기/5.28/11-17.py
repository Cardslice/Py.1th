print("예제 11-17")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")

def getGrade(score) :
    if score>=90 : return('A')
    elif  score>=80 : return('B')
    elif  score>=70 : return('C')
    elif  score>=60 : return('D')
    else : return('F')
name = ["차범근", "이강인", "손흥민", "이동국", "박지성"]#이름 리스트
score = [88, 75, 92, 64, 82]#성적 리스트
n = len(name)
total = 0
for i in range(n) :
    total = total + score[i]
    grade = getGrade(score[i])
    print("%3s : %3d : %3s" % (name[i], score[i], grade))
avg = total / n
print("\n학생 수 :", n)
print("학생 평균 :", avg)
