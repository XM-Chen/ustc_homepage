#!/bin/bash
# 每次本地文档编辑完成后，执行该文件，可上传至ftp://home.ustc.edu.cn/

# ## copy根目录README.md到~chenxman文件夹中
# cp docs/README.md docs/~chenxman/README.md

## 生成静态html文件
npm run docs:build

## 将./index.html和./~chenxman/index.html文件中所有的="/~chenxman/改为="./
sed -i "s:=\"\/~chenxman\/:=\"\.\/:g"  docs/.vuepress/dist/index.html



## 上传到ftp服务器
python3 upload_to_ftp.py