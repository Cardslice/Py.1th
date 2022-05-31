print("예제 11-25")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")

def getAverage(*num) :
    total = 0
    for i in num :
        total = total + i
    avg = total / len(num)
    return avg

print(getAverage(10, 20, 30))
print(getAverage(10, 20, 30, 40, 50))
print(getAverage(10, 20, 30, 40, 50, 60, 70, 80))
