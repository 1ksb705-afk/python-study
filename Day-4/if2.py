# jumin=input("주민번호를 입력하세요") 
# num = jumin.split("-")[1]
# #num = jumin.split("-")
# #081212->[0]
# #3211111[1] ->num
# if num[0] =='1' or num[0] == '3':
#     #num[1][0]
# #(jumin[7]=='1' or jumin[7]=='3'):
#     print("남성")
# else:
#     print("여성")


# 사용자로부터 세 개의 숫자를 입력 받은 후
# 가장 큰 숫자를 출력하라


num1=input("숫자1을 입력하세요")
num2=input("숫자2를 입력하세요")
num3=input("숫자3을 입력하세요")
# 10 30 50
if num1 >= num2 and num1 > num3:
    print("큰수는: ",num1)
elif num2 >= num1 and num2 >= num3:
    print("큰수는: ",num2)
else:
    print("큰수는: ",num3)