import random
answer = random.randint(1,100)
count=0
while True:
    count+=1 
    num = int(input("請輸入數字: "))
    if answer == num:
        print('終於猜對了')
        print('這是你猜的第', count, "次")
        break
    elif answer > num:
        print('比答案小')
    elif answer < num: 
        print('比答案大')
    print('這是你猜的第', count, "次")