amer_price = 2000
cafe_price = 3000
capu_price = 3500
americanos = int(input("아메리카노 판매 개수: "))
cafelattes = int(input("카페라뗴 판매 개수: "))
capucinos = int(input("키푸치노 판매 개수: "))
sales = americanos * amer_price
sales = sales + cafelattes * cafe_price
sales = sales + capucinos * capu_price
print("총 매출액은", sales,"원입니다.") 