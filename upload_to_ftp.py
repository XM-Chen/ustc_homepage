'''
创建时间：2023.1.12
目的：上传文件到ftp服务器
'''
from pythonFTP.FTPTools import FTPTools

obj = FTPTools('home.ustc.edu.cn', 'chenxman', '090071')

# # 删除
# ftpFolder = '/public_html/'
# obj.run(ftpFolder, '', 'delete folder')

# 上传
localPath = 'docs/.vuepress/dist/'  # 递归上传`docs/.vuepress/dist/` 文件夹下的所有文件
ftpPath = '/public_html/'
obj.run(ftpPath, localPath, 'upload folder')