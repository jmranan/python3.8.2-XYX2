

import os


 

 

import requests

from contextlib import closing


def dl(url, path):

 


    def Down_load(file_url,file_path):

        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

        with closing(requests.get(file_url,headers=headers,stream=True)) as response:

            chunk_size = 1024  

            content_size = int(response.headers['content-length'])  

            data_count = 0

            with open(file_path, "wb") as file:

                for data in response.iter_content(chunk_size=chunk_size):

                    file.write(data)

                    data_count = data_count + len(data)

                    now_jd = (data_count / content_size) * 100

                    print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, file_path), end=" ")

     

 



    headers = {

        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
    

    file_url = url
        

    file_path = path

    try:
        Down_load(file_url,file_path)
    except:
        return "error"
    else:
        return "ok"
        

url = "" #这里要加双引号 具体看下方说明

name = "" #这里要加双引号 具体看下方说明

az = False #这里可以写True和False,没有双引号 具体看下方说明

dk = True #这里可以写True和False,没有双引号 具体看下方说明


# url:下载网站
# name:下载后文件姓名
# az:是否为安装包(如果是的话安装以后会自动删除文件)
# dk:下载完毕以后是否需要打开文件(只在az=False下可用)












print("此为姜睦然制作")
print(f"开始下载{name}")
dll = dl(url,name)

if az == True:

    if dll == "ok":
        print(f"\n下载完毕,开始安装{name}")
        os.system(name)
        os.system(f"del {name}")
    else:
        os.system(f"del {name}")
        input("\n下载失败，请确定网络正常")
elif az == False:
    if dll == "ok":
        input("\n下载完毕")
        if dk == True:
            os.system(name)
        
    else:
        os.system(f"del {name}")
        input("\n下载失败，请确定网络正常")
    
    
