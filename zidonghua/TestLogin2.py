from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from zidonghua.InitPage import InitPage
from zidonghua.LoginOperation import LoginOperation
from selenium import webdriver

@ddt
class TestLogin(TestCase):
    @data(*InitPage.login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        # 执行登陆
        driver = webdriver.Chrome()
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        #  获取实际结果
        result = loginop.getError_result()

        driver.quit()

        self.assertEqual(result, expect)

