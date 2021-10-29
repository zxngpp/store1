from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread


# 加载所有用例

class TestLogin(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestLogin.py")

        runner = HTMLTestRunner.HTMLTestRunner(
            title="HKR系统测试成功报告",
            description="HKR系统登陆成功测试",
            verbosity=1,
            stream=open(file="HKR系统测试成功报告.html", mode="w+", encoding="utf-8")
        )

        runner.run(tests)


class TestLogin2(Thread):
    def run(self):
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestLogin2.py")

        runner = HTMLTestRunner.HTMLTestRunner(
            title="HKR系统测试失败报告",
            description="HKR系统登陆失败测试",
            verbosity=1,
            stream=open(file="HKR系统测试失败报告.html", mode="w+", encoding="utf-8")
        )

        runner.run(tests)


T1 = TestLogin()
T2 = TestLogin2()
T1.start()
T2.start()
