from selenium import webdriver
from base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    url='/news/'

    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.NAME,'Submit')

    def type_uesername(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def user_login(self,username,password):
        self.open()
        self.type_uesername(username)
        self.type_password(password)
        self.type_submit()

        sleep(3)

    login_pass_loc=(By.LINK_TEXT,'退出')
    login_false_loc=submit_loc

    def type_loginpass_hint(self):
        return self.find_element(*self.login_pass_loc).text

    def type_loginfalse_hint(self):
        return self.find_element(*self.login_false_loc).text

if __name__ == '__main__':
    driver=webdriver.Firefox()
    loginPage=LoginPage(driver)
    username='feiquan'
    password='*****'
    loginPage.user_login(username,password)
    # print(loginPage.type_loginpass_hint())
    print(loginPage.type_loginfalse_hint())
    sleep(5)
    driver.quit()