print("예제 11-31")

hobby = {'바둑':10, '독서':8, '영화감상':7}

print(hobby)
hobby['영화감상'] = "100명" #원소값 변경
print(hobby)
hobby['등산'] = 20
hobby['여행'] = 30
print(hobby)
del(hobby['바둑'])
print(hobby)
