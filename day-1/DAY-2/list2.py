movie_list=["아바타","왕사남","살묵지","극한직업"]
print(movie_list)
# 메서드(insert,append,remove)
movie_list.insert(1,"범죄도시") #삽입
print(movie_list)

movie_list.append("슈퍼맨") #추가
print(movie_list)

movie_list.remove("살묵지") #값을 지정하여 삭제
print(movie_list)

#del : 명령어
del movie_list[2]
print(movie_list) #요소 위치(인덱스) 지정 삭제

x=10
print(x)
del x
# print(x)

print(len(movie_list)) #len: 길이

a=[1,2,3]
print(sum(a))

# 90,50,80,70
# 평균 구하기
# sum,len 이용
a=[90,50,80,70]
avg=sum(a) /len(a)
print(avg)
