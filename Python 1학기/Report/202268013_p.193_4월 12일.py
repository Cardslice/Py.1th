#-------------------------------- -------#
#   프로그램 : p.193 성적처리 프로그램
#   작성자 : 202268013 조시현
#   작성일: 2022/04/12
#----------------------------------------#

name=input("이름 입력: ") # 학생의 이름
eng=int(input("영어 성적: ")) # 입력받을 영어 성적
math=int(input("수학 성적: ")) # 입력받을 수학 성적
sci=int(input("과학 성적: ")) # 입력받을 과학 성적
total=eng+math+sci # 총점
avg=total/3 # 평균
print("*"*45,end="\n\n")
print(name,"님의 성적처리 결과",end="\n\n")
print("-"*45)
print(" 이름\t영어\t수학\t과학\t총점\t평균")
print("-"*45,end="\n\n")
print(" %s%3d%8d%8d%9d%7d" % (name,eng,math,sci,total,avg),end="\n\n")
print("*"*45)
