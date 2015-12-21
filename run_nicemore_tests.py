#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Created on 2015年11月25日
Function:执行所有测试用例并且发送测试报告
@author: lina
To me :Believe yourself!
'''
from public import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# =============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("lina@ycfis.com", "ln1315")
    smtp.sendmail("lina@ycfis.com", "2354640179@qq.com", msg.as_string())
    smtp.quit()
    print('email has send out !')


# ======查找测试报告目录，找到最新生成的测试报告文件====
def new_report(testreport):
    lists = os.listdir(testreport) 
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    print(lists[-1])
    file_new = os.path.join(testreport, lists[-1])
    #print(file_new)
    return file_new
      
def createSuite():
    # 定义单元测试容器
    testunit = unittest.TestSuite()
    
    test_dir_path = "."
    # 定义搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(test_dir_path, pattern="Execution*.py", top_level_dir=None)
    
    # 讲测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print(testunit)
    return testunit

if __name__ == '__main__':
    result = "result\\"
    test_case = createSuite()
    t=time.localtime(time.time())
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S",t)
    day = time.strftime("%Y-%m-%d",t)
    # 定义 报告的存放路径，支持相对路径
    tdresult = result + day
    
    if os.path.exists(tdresult):
        filename = tdresult + "\\" + now + "_result.html"
        fp = open(filename, "wb")
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='环境：windows 7 浏览器：chrome')
        runner.run(test_case)
        fp.close()  # 关闭生成的报告
        file_path = new_report(tdresult)  # 查找新生成的报告
        #print(file_path)
        send_mail(file_path)  # 调用发邮件模块
    else:
        os.mkdir(tdresult)
        filename = tdresult + "\\" + now + "_result.html"
        fp = open(filename, "wb")
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='环境：windows 7 浏览器：chrome')
        runner.run(test_case)
        fp.close()  # 关闭生成的报告
        file_path = new_report(tdresult)  # 查找新生成的报告
        #print(file_path)
        send_mail(file_path)  # 调用发邮件模块
