# #함수
# def add(a, b): #()안에는 매개변수가 있어야 한다.
#     return a+b
    

# n1=input("숫자1 입력  ")
# n2=input("숫자2 입력  ")
# sum1=add(n1,n2)        #함수 호출(인수), 리턴값을 저장
# print(sum1)

#sum(): 합계
#len(): 길이
#숫자 리스트의 평균을 반환
# 1. 리스트의 합계를 구한다 (sum() 함수 활용 가능)
# 2. 리스트의 개수를 구한다 (len() 함수 활용 가능)
# 3. 합계를 개수로 나눈 값을 return 한다
def avg(numbers):                #함수 선언
    if not numbers:
        return 0
    total=sum(numbers)     #합계
    cnt=len(numbers)       #길이(개수)
    return total/cnt       #평균 구하여 반환(리턴)







score_list=[80,90,100,50,70]
aver_res =avg(score_list) #함수 호출, 반환된 값을 저장
print(aver_res)           #평균 출력