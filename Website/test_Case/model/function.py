from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#截图
def insert_img(driver,filename):
    # driver=webdriver.Firefox()

    #获取当前function.py的文件路径
    fun_path=os.path.dirname(__file__)
    print(fun_path)
    #取得文件的上一级目录
    base_path=os.path.dirname(fun_path)
    print(base_path)
    #将目录变为字符串
    path=str(base_path)
    #将目录中的转义字符替换为原始字符
    # path=path.replace('\\','/')
    #将目录按Website分离
    path=path.split('Website')[0]
    #重组路径
    filepath=path+'Website/test_Report/screen_short/'+filename
    print(filepath)

    driver.get_screenshot_as_file(filepath)
    print('截图%s'%filename+'完成')

#获取最新测试报告的路径
def last_test_report(test_report_dir):
    #获取路径下的所有文件和文件夹列表
    lists=os.listdir(test_report_dir)
    # print(lists)
    #排除结尾'screen_short文件夹的影响
    lists.pop(-1)
    print(lists)
    #按时间排序
    lists.sort(key= lambda fn:os.path.getatime(test_report_dir+'\\'+fn))
    print('The last test report is %s'%lists[-1])
    #获得最新文件路径
    file_path=test_report_dir+'/%s'%lists[-1]
    # file_path=os.path.join(test_report_dir,lists[-1])
    print(file_path)
    return file_path

#发送带附件的邮件
def send_email(last_test_report_path):
    smtpserver='smtp.163.com'

    user='18435227826@163.com'
    password='*****'

    sender=user
    receives=['feiquan2283320@126.com','feiquan2283320@sina.com']

    subject='Selenium Auto Test Report'
    f=open(last_test_report_path,'rb')
    content=f.read()

    att=MIMEText(content,'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    filename=last_test_report_path.split('/')[-1]
    att['Content-Disposition']='attachment;filename="%s"'%filename
    f.close()

    msg=MIMEMultipart()
    msg.attach(MIMEText(content,'html','utf-8'))
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=','.join(receives)
    msg.attach(att)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    print('Start send last test report >>>>>>>>>')
    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()
    print('Send last test report end !')


if __name__ == '__main__':
    # driver=webdriver.Firefox()
    # driver.get('https://www.sogou.com/')
    # filename='sogo.png'
    #
    # insert_img(driver,filename)
    test_report_path=r'E:/Program/Python Program/AutoTest_progect/Website/test_Report/'
    # test_report_path=''
    last_path=last_test_report(test_report_path)

    # send_email(last_path)