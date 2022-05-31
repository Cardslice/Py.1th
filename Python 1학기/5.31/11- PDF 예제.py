print("예제 화면 PDF")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")
friend = {}

friend["김갑룡"] = "010-2346-2354"
friend["이순철"] = "010-3465-0998"
friend["손흥민"] = "010-0987-4321"

for key in sorted(friend.keys()):
    print(key, friend[key])
