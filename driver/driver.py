from selenium import webdriver

def Browse():
    driver=webdriver.Firefox()
    # driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    # driver=webdriver.PhantomJS()

    # driver.get('https://www.baidu.com/')

    return  driver

#模块测试
if __name__ == '__main__':
     Browse()