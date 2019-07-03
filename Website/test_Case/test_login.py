import unittest
from model import function
from model.myunit import StartEnd
from pageobject.login_page import *
from time import sleep

class LoginTest(StartEnd):
    def test_login1_user_normal(self):
        '''username and password is normal '''
        print('Start test case: test_login1_user_normal >>>>>>>')
        po=LoginPage(self.driver)
        po.user_login('51zxw','123456')
        sleep(3)

        #断言与截图
        self.assertEqual(po.type_loginpass_hint(),'退出')
        function.insert_img(po.driver,'test_login1_user_normal.png')
        print('test_login1_user_normal test case end!')

    # @unittest.skip('this test is skip')
    def test_login2_user_error(self):
        '''username is true, password is error'''
        print('Start Test case: test_login2_user_error >>>>>>>')
        po=LoginPage(self.driver)
        po.user_login('51zxe','1458')
        sleep(3)

        self.assertEqual(po.type_loginfalse_hint(),'')
        function.insert_img(po.driver,'test_login2_user_error.png')
        print('test_login2_user_error test case is end！')

    # @unittest.skip('this test is skip')
    def test_login3_user_empty(self):
        '''username and password is empty'''
        print('Start test case: test_login3_user_empty >>>>>>>>')
        po=LoginPage(self.driver)
        po.user_login('','')
        sleep(3)

        self.assertEqual(po.type_loginfalse_hint(),'')
        function.insert_img(po.driver,'test_login3_user_empty.png')
        print('test_login3_user_empty test case is end!')

if __name__ == '__main__':
    unittest.main()