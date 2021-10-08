
'''
    中国工商银行账户管理系统：
        ICBC:
'''

import random
import DUBtils1
# 1.准备一个数据库 和 银行名称
bank_name="中国工商银行昌平回龙观分行"#银行名称写死的
#2.程序入口
def welcome():
    print("************************")
    print("*   中国工商银行昌平分行   *")
    print("************************")
    print("*  1.开户               *")
    print("*  2.存钱               *")
    print("*  3.取钱               *")
    print("*  4.转账               *")
    print("*  5.查询               *")
    print("*  6.Bye!              *")
    print("************************")

# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate,money):

    # 1.判断数据库是否已满
    sql1 = "select count(*) from user "
    param1 = []
    data1 = DUBtils1.select(sql1, param1)
    if data1[0][0] >= 100:
        return 3
    # 2.判断用户是否存在
    sql2 = "select * from user where username=%s"
    param2 = [username]
    data2 = DUBtils1.select(sql2, param2)
    if len(data2) != 0:
        return 2
    # 3.正常开户
    sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
    param3 = [username, account, password, country, province, street, gate, money, bank_name]
    DUBtils1.update(sql3, param3)
    return 1
#用户的开户的操作逻辑

def addUser():
    username=input("请输入您的用户名：")
    password=int(input("请输入您的开户密码："))
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的初始余额："))
    account = random.randint(10000000, 99999999)
    print("您的账户为：", account)
    status = bank_addUser(account, username, password, country, province, street, gate,money)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
                               ----------个人信息------
                               用户名：%s
                               密码：%s
                               账号：%s
                               地址信息
                                   国家：%s
                                   省份：%s
                                   街道：%s
                                   门牌号: %s
                               余额：%s
                               开户行地址：%s
                               ------------------------
                           '''
        print(info % (username, password, account, country, province, street, gate,money, bank_name))

# 用户的存钱操作逻辑
def cunkuan():
    account = int(input("请输入您的用户账号："))
    saver = int(input("请输入您存钱的金额："))
    sql4 = "select * from user where account=%s"
    param4 = [account]
    data=DUBtils1.select(sql4,param4)
    if len(data) != 0:
        sql5 = "update user set money = money + %s where account=%s"
        param5 = [saver,account]
        DUBtils1.update(sql5,param5)
        print("存款成功！")
    else:
        print("对不起，用户库不存在该账户！")
# 用户的取钱操作逻辑
def fetch():
    account = int(input("请输入您的用户账号："))
    sql6 = "select * from user where account=%s"
    param6 = [account]
    data = DUBtils1.select(sql6, param6)
    if len(data) != 0:
        password = int(input("请输入您的账号密码："))
        if password==data[0][2]:
            draw = int(input("请输入您取钱的金额："))
            if draw<=data[0][7]:
                sql7 = "update user set money = money - %s where account=%s"
                param7 = [draw, account]
                DUBtils1.update(sql7, param7)
                print("取款成功！")
            else:
                print("钱不够！")
        else:
            print("密码输入错误！")
    else:
        print("账号不存在！")
# 用户的转账操作逻辑
def rotate():
    account = int(input("请输入您的转入账号："))
    sql8 = "select * from user where account=%s"
    param8 = [account]
    data = DUBtils1.select(sql8, param8)
    if len(data) != 0:
        account1 = int(input("请输入您的转出账号："))
        sql9 = "select * from user where account=%s"
        param9 = [account1]
        data1 = DUBtils1.select(sql9, param9)
        if len(data1) != 0:
            password = int(input("请输入您的转出账号密码："))
            if password == data1[0][2]:
                turn = int(input("请输入您转账的金额："))
                if turn <= data1[0][7]:
                    sql10 = "update user set money = money + %s where account=%s"
                    param10 = [turn, account]
                    DUBtils1.update(sql10, param10)
                    sql11 = "update user set money = money - %s where account=%s"
                    param11 = [turn, account1]
                    DUBtils1.update(sql11, param11)
                    print("转账成功！")
                else:
                    print("钱不够！")
            else:
                    print("密码输入错误！")
        else:
                print("转出账号不存在！")
    else:
            print("转入账号不存在！")
#用户查询的操作逻辑
def demand():
    account = int(input("请输入您的用户账号："))
    sql12 = "select * from user where account=%s"
    param12 = [account]
    data = DUBtils1.select(sql12, param12)
    if len(data) != 0:
        password = int(input("请输入您的账号密码："))
        if password == data[0][2]:
            info = '''
                                           ----------个人信息------
                                           账号：%s
                                           密码：%s
                                           余额：%s
                                           地址信息
                                               国家：%s
                                               省份：%s
                                               街道：%s
                                               门牌号: %s
                                           开户行地址：%s
                                           开户日期：%s
                                           ------------------------
                                       '''
            print(info % (data[0][1], password, data[0][7], account, data[0][4], data[0][5], data[0][6], bank_name,data[0][9]))
        else:
            print("密码输入错误！")
    else:
        print("该用户不存在!")

while True:
    #打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        cunkuan()
    elif chose == "3":
        fetch()
    elif chose == "4":
        rotate()
    elif chose == "5":
        demand()
    elif chose == "6":
        print("欢迎下次光临!")
        break
    else:
        print("输入错误！请重新输入！")