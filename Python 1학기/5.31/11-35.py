print("예제 11-35")
print("학번 : 202268013, 이름 : 조시현")
print("*******************************")
def writeRecord(**arg) :
    print("-"*30)
    for k in arg.keys() :
        print("%-10s :" % (k), arg[k])
    print("-"*30)
writeRecord(name = "이강인", job= "축구선수", address = "스페인")
writeRecord(university = "한국대학교",
            deptment = "컴퓨터공학과", entry = 40)
writeRecord(이름 = "이강인", 국어=94, 영어=88, 수학=84, 과학=78, 사회= 92)
