######import######
import hashlib
from random import randint
import os
##################

########def#######

def hashmd5(s2a):
    hash = hashlib.md5(f"!@{s2a}".encode("utf-8")).hexdigest()
    return hash

def jmmd5(stra):
    return hashmd5(stra)
def yz(stra,md5):
    if jmmd5(stra) == md5:
        return True
    else:
        return False
def filewrite(filename,nr):
    f = open(filename,"w")
    f.write(nr)
    f.close()
def fileread(filename):
    f = open(filename,"r")
    return f.read()

def filefind(filename):
    try:
        f = open(filename,"r")
    except:
        return False
    else:
        f.close()
        return True
def lpsc(cd):
    zz = ""
    zsb = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9")
    for i in range(cd):
        zz = zz + zsb[randint(0,len(zsb)-1)]
    return zz


####################

##########main########

if filefind("dl.dll"):
    if filefind("dll.dll"):
        lpa = input("请输入令牌：")
        os.system("cls")
        if jmmd5(lpa) == fileread("dll.dll"):
            os.remove("dll.dll")
            input("令牌正确")    #把这行删掉，换成验证通过后的代码
        else:
            input("令牌错误")
    else:
        ypass = input("请输入密码：")
        os.system("cls")
        if yz(ypass,fileread("dl.dll")):
            lp = lpsc(100)
            filewrite("令牌.txt",lp)
            filewrite("dll.dll",jmmd5(lp))
            input("令牌已生成，请去令牌.txt寻找,注意查收")
        else:
            input("密码错误")
else:
    mm = input("请输入你要设定的密码:")
    os.system("cls")
    mmqd = input("请再次输入你要设定的密码：")
    os.system("cls")
    if mm == mmqd:
        filewrite("dl.dll",jmmd5(mm))
        input("密码设定成功，请从新启动程序")
        quit()
    else:
        input("两次密码不相同")
        quit()







########################


