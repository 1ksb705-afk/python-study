import gugu_modul
from gugu_modul import *
r=True
while r :
    num=int(input("숫자를 선택하세요(1:세로 구구단 2:가로구구단 0:종료)"))
    if num == 1:
        v_gugudan()           #v_gugudan함수 호출
    elif num == 2:
        h_gugudan()           #h_gugudan함수 호출
    elif num == 0:
        print("시스템 종료")
        r = False
    else:
        print("잘못 선택: 다시 입력")