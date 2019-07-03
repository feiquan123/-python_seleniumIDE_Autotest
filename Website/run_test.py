import unittest
from BSTestRunner import BSTestRunner
from model import function
import time

report_dir='./test_Report'
test_dir='./test_Case'

discovery=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
filename=report_dir+'/'+now+'result.html'

print('开始生成测试报告>>>>>>>>')
with open(filename,'wb')as f:
    runner=BSTestRunner(stream=f,title='Selenium Auto Test Report',description='localhost test result')
    runner.run(discovery)
    f.close()
print('测试报告生成结束.....')

last_report=function.last_test_report(report_dir)
print(last_report)
print('Start send email >>>>>>')
function.send_email(last_report)
print('Send email end .....')
