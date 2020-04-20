import datetime
dt = datetime.datetime.now()
s = str(dt.year) + "年" + str(dt.month) + "月" + str(dt.day) + "日" + str(dt.hour) + "时" + str(dt.minute) + "分" + str(dt.second) + "秒" + "的计算器使用记录"
with open(f"{s}.txt","w") as an:

    while True:
        b = input("请输入公式，输入exit退出:")
        if b == "exit":
            quit()
        else:
            y = ""
            w = []
            if "=" in b:
                b = list(b)
                del b[len(b) - 1]
                for i in b:
                    y = y + i
            else:
                y = b
            try:
                z = eval(y)
            except:
                print("error")
                continue
            else:
                print(f"得数：{z}")
                an.write(f"{y}={z}")
                an.write("\n")
                an.flush()


