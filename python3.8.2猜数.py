from random import randint
from time import time
c = 0
nowtime = time()
try:
    nd = int(input("请输入难度(范围是10~10000的整数)："))
except:
    input("INTERROR!!!")
    quit()

if nd > 10000 or nd < 10:
    input("INTERROR!!!")
    quit()

rd = randint(0,(nd - 1))
while True:
    try:
        c = c + 1
        hd = int(input("你能猜到我心里想的数吗，如果可以请输入："))
    except:
        c = c - 1
    else:
        if hd > rd:
            print("猜错了哟，提示：你猜大了")
        elif hd < rd:
            print("猜错了哟，提示：你猜小了")
        elif hd == rd:
            input(f"恭喜你答对了,本次猜了{c}次、用时：{(time() - nowtime)}秒")
            quit()
   



    
    
