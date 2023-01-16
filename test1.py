# -*- coding: utf-8 -*-
import ftplib

# def remove_all(ftp, path):
#     """
#     删除ftp服务器上指定路径下的所有文件
#     :param ftp: ftplib.FTP对象
#     :param path: 要删除的文件路径
#     :return:
#     """
#     # 切换目录
#     ftp.cwd(path)
#     # 获取当前目录下的所有文件和文件夹
#     names = ftp.nlst()
 
#     for name in names:
#         # 如果是文件夹，则进入该文件夹，递归删除
#         if '.' not in name:
#             remove_all(ftp, path + '/' + name)
#         # 如果是文件，则删除
#         else:
#             ftp.delete(name)
 
#     # 删除完文件后，返回上一级目录
#     ftp.cwd('..')
#     # 删除文件夹
#     ftp.rmd(path)


# if __name__ == '__main__':
#     ftp = ftplib.FTP('home.ustc.edu.cn')
#     remove_all(ftp, '/public_html')

def delAllfile(ftp,ftppath):
    try:
        print (ftppath)
        try:
            ftp.cwd(ftppath)
        except Exception as e:
            print ("进入ftp目录失败" + str(e))
        ftp.dir('.', dir_res.append)  # 对当前目录进行dir()，将结果放入列表
        print(dir_res)
        for i in dir_res:
            if i.startswith("d"):
                dirName=i.split(" ")[-1]
                print("开始删除"+dirName+"文件夹")
                delAllfile(ftp,ftp.pwd() + "/" + dirName)
                ftp.cwd('..')
                print(ftppath+"/"+dirName)
                ftp.rmd(ftppath + '/' + dirName)
            else:
                filelist = ftp.getfiles(ftppath)
                for f in filelist:
                    print ("删除FTP目录："+ftppath+"下存在文件:"+f)
                    ftp.delete(f)
    except Exception as e:
        raise e
 

if __name__ == '__main__':
    ftp = ftplib.FTP('home.ustc.edu.cn')
    delAllfile(ftp, '/public_html')
