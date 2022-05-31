print("예제 11-29")
print("학번 : 202268013, 이름 : 조시현")
print("-------------------------------")
nickNameSet = {'수선화', '코스모스', '들국화', '감자'}
userNickname = input("원하는 닉네임을 입력해 주세요: ")
while True :
    if userNickname in nickNameSet :
        print("이미 사용중인 닉네임입니다")
        userNickname = input("원하는 닉네임을 입력해 주세요: ")
    else :
        print("사용 가능한 닉네임입니다. 닉네임으로 등록합니다.")
        nickNameSet = nickNameSet | { userNickname }
        break
print("사용 중인 닉네임: ", nickNameSet)
