# num1 = int(input("짝수 입력: "))
# num2 = int(input("홀수 입력: "))
# match num1%2, num2%2:
#     case 0,1:
#         print("num1은 짝수 num2는 홀수")
#     case 0,_:
#         print("num1은 짝수 num2는 아무숫자")
#     case _,1:
#         print("num2는 홀수 num1은 아무숫자")
#     case _:
#         print("둘 다 오류")

num1 = int(input("3의 배수 입력: "))
num2 = int(input("5의 배수 입력: "))
match num1%3, num2%5:
    case 0,0:
        print("num1은 3의 배수 num2는 5의 배수")
    case 0,_:
        print("num1은 3의 배수 num2는 아무숫자")
    case _,0:
        print("num2는 5의 배수 num1은 아무숫자")
    case _:
        print("둘 다 오류") #break는 필요없다.
