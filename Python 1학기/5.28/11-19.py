print("예제 11-19")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")
class1 = [[54, 56, 98, 87, 78], [10, 20, 30, 40, 50], [11, 12, 13, 14, 15]]
classSum = 0; i = 0; numSubj = 0
for stu in class1 :
    sum = 0
    for subj in stu  :
        sum = sum + subj
    avg = sum / len(stu)
    print("%d번 학생 : 총점 = %d, 평균 = %6.2f" % (i, sum, avg))
    i = i + 1
    numSubj += len(stu)
    classSum = classSum + sum
avgClass = classSum / (numSubj)
print("전체 평균 = %6.2f" % (avgClass))
