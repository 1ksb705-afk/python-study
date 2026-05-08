# st= input("영어 한 글자를 입력하세요: ")
# if st.isupper(): #대문자인가?->ture 아니면 ->false
#     print("st.lower") #true일 때 소문자로 변경 
# else : #소문자인가?
#     print("st.upper") #대문자로 변경


score = int(input("점수를 입력하세요: "))
if 81 <=score <=100:
    print("A 학점입니다")
elif 61<=score<=80:
    print("B 학점입니다")
elif 41<=score<=60:
    print("C 학점입니다")
elif 21<=score<=40:
    print("D 학점입니다")
else:
    print("E 학점입니다") 
