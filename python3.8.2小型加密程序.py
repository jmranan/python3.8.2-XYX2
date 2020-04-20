######import######
import hashlib
from random import randint
import os

##################

########def#######
def r(stra):
    if stra == 'A':
        return "amd081"
    elif stra == 'a':
        return "cdef081"
    elif stra == 'B':
        return "shs081"
    elif stra == 'b':
        return "shshb081"
    elif stra == 'E':
        return "hsahs081"
    elif stra == 'e':
        return "sh081"
    elif stra == "F":
        return "wws081"
    elif stra == "f":
        return "htps081"
    elif stra == "G":
        return "rtf081"
    elif stra == "g":
        return "txt081"
    elif stra == "H":
        return "exe081"
    elif stra == "h":
        return "baba081"
    elif stra == "I":
        return "dada081"
    elif stra == "i":
        return "ssh081"
    elif stra == "J":
        return "vnc081"
    elif stra == "j":
        return "cps081"
    elif stra == "K":
        return "rst081"
    elif stra == "k":
        return "amd082"
    elif stra == "L":
        return "cdef082"
    elif stra == "l":
        return "cdef082"
    elif stra == "M":
        return "shshb082"
    elif stra == "m":
        return "hsahs082"
    elif stra == "N":
        return "sh082"
    elif stra == "n":
        return "wws082"
    elif stra == "O":
        return "htps082"
    elif stra == "o":
        return "rtf082"
    elif stra == "P":
        return "txt082"
    elif stra == "p":
        return "exe082"
    elif stra == "Q":
        return "baba082"
    elif stra == "q":
        return "dada082"
    elif stra == "R":
        return "ssh082"
    elif stra == "r":
        return "vnc082"
    elif stra == "S":
        return "cps082"
    elif stra == "s":
        return "rst082"
    elif stra == "T":
        return "amd083"
    elif stra == "t":
        return "cdef083"
    elif stra == "U":
        return "shs083"
    elif stra == "u":
        return "shshb083"
    elif stra == "V":
        return "hsahs083"
    elif stra == "v":
        return "sh083"
    elif stra == "W":
        return "wws083"
    elif stra == "w":
        return "htps083"
    elif stra == "X":
        return "rtf083"
    elif stra == "x":
        return "txt083"
    elif stra == "Y":
        return "exe083"
    elif stra == "y":
        return "baba083"
    elif stra == "Z":
        return "dada083"
    elif stra == "z":
        return "ssh083"
    elif stra == "1":
        return "vnc083"
    elif stra == "2":
        return "cps083"
    elif stra == "3":
        return "rst083"
    elif stra == "4":
        return "amd084"
    elif stra == "5":
        return "cdef084"
    elif stra == "6":
        return "shs084"
    elif stra == "7":
        return "shshb084"
    elif stra == "8":
        return "hsahs084"
    elif stra == "9":
        return "sh084"
    elif stra == "0":
        return "wws084"
    elif stra == ".":
        return "htps084"
    elif stra == "C":
        return "rtf084"
    elif stra == "c":
        return "txt084"
    elif stra == "D":
        return "exe084"
    elif stra == "d":
        return "baba084"

    else:
        return "暂不支持此符号"


def w(strb):
    if strb == r("A"):
        return "A"
    elif strb == r("a"):
        return "a"
    elif strb == r("B"):
        return "B"
    elif strb == r("b"):
        return "b"
    elif strb == r("C"):
        return "C"
    elif strb == r("c"):
        return "c"
    elif strb == r("D"):
        return "D"
    elif strb == r("d"):
        return "d"
    elif strb == r("E"):
        return "E"
    elif strb == r("e"):
        return "e"
    elif strb == r("F"):
        return "F"
    elif strb == r("f"):
        return "f"
    elif strb == r("G"):
        return "G"
    elif strb == r("g"):
        return "g"
    elif strb == r("H"):
        return "H"
    elif strb == r("h"):
        return "h"
    elif strb == r("I"):
        return "I"
    elif strb == r("i"):
        return "i"
    elif strb == r("J"):
        return "J"
    elif strb == r("j"):
        return "j"
    elif strb == r("K"):
        return "k"
    elif strb == r("k"):
        return "k"
    elif strb == r("L"):
        return "l"
    elif strb == r("l"):
        return "l"
    elif strb == r("M"):
        return "M"
    elif strb == r("m"):
        return "m"
    elif strb == r("N"):
        return "n"
    elif strb == r("n"):
        return "n"
    elif strb == r("O"):
        return "O"
    elif strb == r("o"):
        return "o"
    elif strb == r("P"):
        return "P"
    elif strb == r("p"):
        return "p"
    elif strb == r("Q"):
        return "Q"
    elif strb == r("q"):
        return "q"
    elif strb == r("R"):
        return "R"
    elif strb == r("r"):
        return "r"
    elif strb == r("S"):
        return "S"
    elif strb == r("s"):
        return "s"
    elif strb == r("T"):
        return "T"
    elif strb == r("t"):
        return "t"
    elif strb == r("U"):
        return "U"
    elif strb == r("u"):
        return "u"
    elif strb == r("V"):
        return "V"
    elif strb == r("v"):
        return "v"
    elif strb == r("W"):
        return "W"
    elif strb == r("w"):
        return "w"
    elif strb == r("X"):
        return "X"
    elif strb == r("x"):
        return "x"
    elif strb == r("Y"):
        return "Y"
    elif strb == r("y"):
        return "y"
    elif strb == r("Z"):
        return "Z"
    elif strb == r("z"):
        return "z"
    elif strb == r("1"):
        return "1"
    elif strb == r("2"):
        return "2"
    elif strb == r("3"):
        return "3"
    elif strb == r("4"):
        return "4"
    elif strb == r("5"):
        return "5"
    elif strb == r("6"):
        return "6"
    elif strb == r("7"):
        return "7"
    elif strb == r("8"):
        return "8"
    elif strb == r("9"):
        return "9"
    elif strb == r("0"):
        return "0"
    elif strb == r("."):
        return "."




    else:
        return "解密错误"


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
            jm12 = input("解密请输入1，加密请输入2:")
            if jm12 == "1":
                jmt = ""
                f = open("加密信息.txt", "a")
                f.close()
                jma = input("请将加密信息添加到一个名为加密信息的文本文件里,格式为一个加密信息一行,OK后请按回车")
                x = file("加密信息.txt")
                filea = ""
                for i in x:
                    filea = filea + w(i)
                f = open("解密.txt", "w")
                f.write(filea)
                f.close()
                input("解密完毕，请到一个名为解密的文本文件里。")





            elif jm12 == "2":
                jm = input("请输入需要加密的内容:")
                jmok = ""
                for i in jm:
                    jmok = jmok + r(i) + "\n"

                else:
                    f = open("加密.txt", "w+")
                    f.write(jmok)
                    f.close()
                    input(f"成功，加密内容以写到名为加密的文本文件里了")

            else:
                input("ERROR")
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

