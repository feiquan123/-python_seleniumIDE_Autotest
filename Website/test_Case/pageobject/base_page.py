# from selenium import webdriver
from time import sleep

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Firefox()

        self.base_url='http://localhost'
        self.timeout=5

    def _open(self,url):
        url_=self.base_url+url
        print('Test webpage is %s'%url_)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(3)
        assert self.driver.current_url==url_ ,'Open not load on %s'%url_

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements()