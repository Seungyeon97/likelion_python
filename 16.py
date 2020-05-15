def avg(sum, cnt):
    return sum/cnt


sum = 0
cnt =0

while True:
    num =int(input("숫자를 입력하세요 :"))
    if num!=-1:
        sum+=num
        cnt +=1
    else:
        break

print(avg(sum,cnt))