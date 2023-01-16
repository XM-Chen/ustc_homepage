'''
创建时间：2023.1.13
目的：测试FTPTools删除ftp服务器上文件的功能
'''
from pythonFTP.FTPTools import FTPTools

obj = FTPTools('home.ustc.edu.cn', 'chenxman', '090071')

# ftpFile = '/public_html/'
# obj.run(ftpFile, '', 'delete file')

# ftpFolder = '/public_html/'
# obj.run(ftpFolder, '', 'delete folder')

# 创建文件夹
ftpPath = '/public_html2/'
obj.run(ftpPath, '', 'create folder') 