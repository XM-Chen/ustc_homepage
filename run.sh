#!/bin/bash
# 每次本地文档编辑完成后，执行该文件，可上传至ftp://home.ustc.edu.cn/


## 生成静态html文件
npm run docs:build

## 将./index.html和./~chenxman/index.html文件中所有的="/~chenxman/改为="./
sed -i "s:=\"\/~chenxman\/:=\"\.\/:g"  docs/.vuepress/dist/index.html



## 上传到ftp服务器
lftp chenxman:090071@home.ustc.edu.cn -e "mirror -R --delete ~/Nutstore\ Files/vuepress/ustc-docs/docs/.vuepress/dist/ /public_html/"
