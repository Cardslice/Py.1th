def checkpassword(pw):
    global count
    count = count + 1
    if pw == "Python" :
        return(1)
    return(0)

count(0)
pw = input("패스워드 입력: ")
state = checkPassword(pw)
while count < 3 :
    if state = 1 :break
    pw = ("패스워드 재입력: ")
    state = checkpassword(pw)

if coint < 3 :
    print("로그인 성공")
else :
    print("부정사용자임(3회 패스워드 오류)")
