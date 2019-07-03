import unittest
from driver import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        print('start test>>>>')
        self.driver=Browse()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
        print('end test..........\n')
# if __name__ == '__main__':
#     unittest.main()
