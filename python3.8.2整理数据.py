

def file(filename):
    f = open(filename, "a")
    f.close()
    f = open(filename, "r")
    z = f.readlines()
    z2 = []
    z3 = ""
    for i in z:
        i = list(i)
        del i[-1:]
        for i2 in i:
            z3 = z3 + i2
        z2.append(z3)
        del z3
        z3 = ""
        globals()

    f.close()
    return z2

file("read.txt")
print("此为姜睦然编写")
print("编程语言：python3.8.2")
input("请将准备查找的内容填到read.txt文件里，格式为一条信息一行，注意：最后一定要加一个换行")

x = file("read.txt")

while True:
    y = input("请输入要查找的项目,输入后按回车:")
    a = 0
    for i in x:
        if y == i:
            a = a + 1
    print(f"结果:{a}")
            
    
