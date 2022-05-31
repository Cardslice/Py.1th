print("실습 코드 1")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")
# 학점 판성 함수
def getGrade(score) :
    if score>=90 : return('A')
    elif  score>=80 : return('B')
    elif  score>=70 : return('C')
    elif  score>=60 : return('D')
    else : return('F')
name, eng, math, total, avg, grade = [], [], [], [], [], []

# n명 이름, 영어성적, 수학성적 입력 및 name, eng, math 리스트 구성
n = int(input("학생 수 입력: "))
for i in range(0, n) :
    print("\n%d번째 학생 자료 입력" % i)
    name.append(input("이름 : "))
    eng.append(int(input("영어 성적 : ")))
    math.append(int(input("수학 성적 : ")))

# 총점, 평균, 학점 계산 및 total, avg, grade 리스트 구성
for i in range(0, n) :
    total.append(eng[i] + math[i])
    avg.append(total[i] / 2)
    grade.append(getGrade(avg[i]))

# 전체 성적표 출력, !함수 정의되지 않음!
def printTItle()
for i in range(0,n) :
    printRecord(name[i], eng[i], math[i], avg[i], total[i], grade[i])

# 최고 득점자 조사 및 출력
max = 0
for i in range(1, n) :
    if total[max] < total[i] : max = i
print("\n최고 평균 : %6.2f(%s)" % (avg[max], name[max]))
