from threading import Thread

import time

import threading   # 线程锁

a = threading.RLock() # 线程锁命名为a

Humburger = 500


class programmer(Thread):
    username = ""
    count = 0

    def run(self) -> None:

        global Humburger  # 使用全局变量
        while 1:  # 死循环
            if Humburger < 498:
                a.acquire()  # 锁上
                self.count = self.count + 1
                Humburger = Humburger + 1
                print("还有", Humburger, "汉堡包")
                # time.sleep(0.01)
                a.release()  # 解锁
            elif Humburger > 500:
                time.sleep(3)
                break
        print("总共制造了", Humburger, "个汉堡包！")


class xiaofei(Thread):
    username = ""
    money = 100
    count = 0

    def run(self) -> None:
        global Humburger
        while 1:  # 死循环
            if self.money > 0 and Humburger > 0:
                a.acquire()
                self.count = self.count + 1
                self.money = self.money - 5
                Humburger = Humburger - 1
                print(self.username, "买了", self.count, "个汉堡包！", "还剩", self.money,"块钱")
                # time.sleep(0.01)
                a.release()
            elif self.money == 0:
                a.acquire()
                print("没有钱了")
                print(self.username, "买了", self.count, "个汉堡包！###########################")
                a.release()
                break
            elif Humburger == 0:
                time.sleep(2)


u1 = programmer()
u1.username = "少岩"

u2 = programmer()
u2.username = "少安"

u3 = programmer()
u3.username = "少承"

x1 = xiaofei()
x1.username = "少煜"

x2 = xiaofei()
x2.username = "少禹"

x3 = xiaofei()
x3.username = "少御"

x4 = xiaofei()
x4.username = "少楷"

x5 = xiaofei()
x5.username = "少旸"

x6 = xiaofei()
x6.username = "少疆"

u1.start()
u2.start()
u3.start()
x1.start()
x2.start()
x3.start()
x4.start()
x5.start()
x6.start()
x6.run()
