# encoding=utf-8
import os
import shutil
from time import sleep

usb_path = "/Volumes/"
content = os.listdir(usb_path)  # os.listdir(路径)返回路径下所有文件以及文件夹的名称
while True:
    new_content = os.listdir(usb_path)  # 每隔三秒扫描一次/Volumes/
    if new_content != content:  # 如果发现异常，即多出一个文件夹，则退出
        break;
    sleep(3)
x = [item for item in new_content if item not in content]
# 找到那个新文件夹，返回包括新文件夹string类型名称的列表，这个表达方法很pythonic
shutil.copytree(os.path.join(usb_path, x[0]), '/Users/home/usb_copy')
# shutil.copytree 把目录下所有东西一股脑复制进/Users/home/usb_copy,
# 放进了自己的home目录下
