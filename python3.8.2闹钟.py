import datetime
import time
import os
input("请确保有音频播放器和闹钟.m4a的音频文件(此文件是时间到后播放的音频),ok后按回车")


s = input("计时器模式请输入1，闹钟模式请输入2:")
if s == "1":
    x = int(input("请输入计时时间(s):"))
    print("定时器设定成功，请勿关闭此窗口")
    time.sleep(x)
    while True:
        os.system("闹钟.m4a")
        time.sleep(120 + 53)
elif s == "2":
    yh = int(input("请输入小时:"))
    ym = int(input("请输入分钟:"))
    print("时钟设定成功，请勿关闭此窗口")
    while True:
        now = datetime.datetime.now()
        h, m = now.hour, now.minute
        if h == yh and m >= ym:
            os.system("闹钟.m4a")
            time.sleep(120 + 53)
        time.sleep(1)





