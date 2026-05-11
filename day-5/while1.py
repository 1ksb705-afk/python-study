# 1~100까지 합과 개수
sum = 0
cnt = 1

while cnt < 101: #1~100 만족할때까지 반복
    sum=sum+cnt # 합을 누적
    cnt = cnt+1 # 1씩 누적

print("개수는 : ",cnt-1)
print("합계는 : ",sum)